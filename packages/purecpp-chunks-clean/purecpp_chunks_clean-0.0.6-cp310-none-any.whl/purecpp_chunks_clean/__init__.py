import os
import sys
import ctypes
from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import shutil

REQUIRED_FILES = [
    # "libaoti_custom_ops.so",
    # "libbackend_with_compiler.so",
    "libc10.so",
    # "libjitbackend_test.so",
    # "libnnapi_backend.so",
    # "libshm.so",
    "libtorch.so",
    "libtorch_cpu.so",
    # "libtorch_global_deps.so",
    # "libtorch_python.so",
    # "libtorchbind_test.so",
]

def download_libtorch():
    # URL e arquivo zip
    libtorch_cpu_zip = "libtorch-cxx11-abi-shared-with-deps-2.5.0+cpu.zip"
    libtorch_cpu_url = (
        "https://download.pytorch.org/libtorch/cpu/"
        "libtorch-cxx11-abi-shared-with-deps-2.5.0%2Bcpu.zip"
    )
    
    # Caminho base: d_libs/
    pkg_dir = os.path.join(os.path.dirname(__file__), "d_libs")
    libtorch_dir = os.path.join(pkg_dir, "libtorch")
    cpu_dir = os.path.join(libtorch_dir, "cpu")
    lib_path = os.path.join(cpu_dir, "lib")  # É aqui que os .so devem estar

    # 1) Verifica se todos os arquivos necessários já existem
    all_files_present = True
    if os.path.exists(lib_path):
        for f in REQUIRED_FILES:
            if not os.path.exists(os.path.join(lib_path, f)):
                all_files_present = False
                break
    else:
        all_files_present = False

    if all_files_present:
        # print("All required files are already present in:", lib_path)
        return
    else:
        print("Not all files are present. Downloading libtorch...")

    # 2) Se faltou algum arquivo, remove tudo e baixa novamente
    if os.path.exists(pkg_dir):
        shutil.rmtree(pkg_dir)
    os.makedirs(libtorch_dir, exist_ok=True)

    # Baixa o arquivo zip
    subprocess.check_call(["wget", libtorch_cpu_url, "-O", libtorch_cpu_zip])

    # Descompacta no libtorch_dir
    subprocess.check_call(["unzip", "-o", libtorch_cpu_zip, "-d", libtorch_dir])

    # Renomeia libtorch -> cpu
    extracted_dir = os.path.join(libtorch_dir, "libtorch")
    if os.path.exists(extracted_dir):
        os.rename(extracted_dir, cpu_dir)
    else:
        print("Error: extracted_dir does not exist")

    # Remove o zip
    os.remove(libtorch_cpu_zip)
    print("Libtorch downloaded and extracted successfully.")

    # Só para debug, lista o que ficou em d_libs/
    result = subprocess.run(["ls", pkg_dir], capture_output=True, text=True)
    print("Conteúdo de d_libs/:", result.stdout)


"""
Script unificado para converter modelos Hugging Face para o formato ONNX.
Você pode alterar as variáveis globais abaixo para configurar os modelos a serem convertidos.
O script cria a pasta "models" (no diretório pai) caso ela não exista e realiza:
  1. Conversão de modelo para extração de características (ex: sentence-transformers).
  2. Conversão de modelo para classificação de tokens (ex: NER).
  
Antes de executar, certifique-se de instalar:
  - torch
  - transformers
  - onnx
  - onnxruntime
  - optimum
"""

import json
from pathlib import Path

# =====================
# Variáveis Globais
# =====================
# Altere estes valores conforme necessário
FEATURE_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
TOKEN_MODEL_NAME   = "dslim/bert-base-NER"
TOKEN_OUTPUT_NAME  = "bert-base-ner-converted"

# Diretório base onde os modelos serão salvos (um diretório "models" no diretório pai deste script)
BASE_DIR = os.path.join(os.path.dirname(__file__), "models")

# Cria o diretório BASE_DIR se ele não existir
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
    print(f"Diretório criado: {BASE_DIR}")

# =====================
# Função para conversão de modelo para extração de características
# =====================
def convert_feature_extraction_model(model_name):
    print(f"\nConvertendo modelo de extração de características: {model_name}")
    from optimum.onnxruntime import ORTModelForFeatureExtraction
    from transformers import AutoTokenizer

    dir_path = os.path.join(BASE_DIR, model_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Diretório criado para o modelo: {dir_path}")

    model = ORTModelForFeatureExtraction.from_pretrained(model_name, export=True)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model.save_pretrained(dir_path)
    tokenizer.save_pretrained(dir_path)
    print(f"Modelo de extração salvo em: {dir_path}")

# =====================
# Função para conversão de modelo para classificação de tokens (ex: NER)
# =====================
def convert_token_classification_model(model_name, output_name):
    print(f"\nConvertendo modelo de classificação de tokens: {model_name}")
    from transformers import AutoModelForTokenClassification, AutoTokenizer, AutoConfig
    from transformers.onnx import export, FeaturesManager

    config = AutoConfig.from_pretrained(model_name)
    label_map = config.id2label
    dir_path = os.path.join(BASE_DIR, model_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Diretório criado para o modelo: {dir_path}")

    # Salva o label map em um arquivo JSON
    label_map_path = os.path.join(dir_path, "label_map.json")
    with open(label_map_path, "w") as f:
        json.dump(label_map, f)
    print(f"Label map salvo em: {label_map_path}")

    model = AutoModelForTokenClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer_save_path = os.path.join(dir_path, "tokenizer")
    tokenizer.save_pretrained(tokenizer_save_path)
    print(f"Tokenizador salvo em: {tokenizer_save_path}")

    model_type = model.config.model_type
    feature = "token-classification"
    outpath = Path(os.path.join(dir_path, "model.onnx"))

    onnx_config = FeaturesManager.get_config(model_type=model_type, feature=feature)
    onnx_config = onnx_config(model.config)

    export(model=model, output=outpath, opset=14, preprocessor=tokenizer, config=onnx_config)
    print(f"Modelo de classificação exportado para: {outpath}")

# =====================
# Função principal
# =====================

# Conversão para extração de características
convert_feature_extraction_model(FEATURE_MODEL_NAME)

# Conversão para classificação de tokens (NER)
convert_token_classification_model(TOKEN_MODEL_NAME, TOKEN_OUTPUT_NAME)
download_libtorch()

LIB_PATH = os.path.join(os.path.dirname(__file__), "d_libs", "libtorch", "cpu", "lib")

# Pegando o valor atual do LD_LIBRARY_PATH ou uma string vazia se não existir
current_ld_library_path = os.environ.get("LD_LIBRARY_PATH", "")

LIB_MODELS = os.path.join(os.path.dirname(__file__), "models")
LIB_LOCAL = os.path.join(os.path.dirname(__file__))
new_ld_library_path = f"{LIB_PATH}:/usr/local/lib:{current_ld_library_path}:{LIB_MODELS}:{LIB_LOCAL}".strip(":")

# Atualizando a variável de ambiente
os.environ["LD_LIBRARY_PATH"] = new_ld_library_path
# Carrega manualmente as bibliotecas necessárias, *antes* de importar o módulo C++
try:
    # ctypes.cdll.LoadLibrary(os.path.join(LIB_PATH, "libaoti_custom_ops.so"))
    # ctypes.cdll.LoadLibrary(os.path.join(LIB_PATH, "libbackend_with_compiler.so"))
    ctypes.cdll.LoadLibrary(os.path.join(LIB_PATH, "libc10.so"))
    # ctypes.cdll.LoadLibrary(os.path.join(LIB_PATH, "libjitbackend_test.so"))
    # ctypes.cdll.LoadLibrary(os.path.join(LIB_PATH, "libnnapi_backend.so"))
    # ctypes.cdll.LoadLibrary(os.path.join(LIB_PATH, "libshm.so"))
    ctypes.cdll.LoadLibrary(os.path.join(LIB_PATH, "libtorch.so"))
    ctypes.cdll.LoadLibrary(os.path.join(LIB_PATH, "libtorch_cpu.so"))
    # ctypes.cdll.LoadLibrary(os.path.join(LIB_PATH, "libtorch_global_deps.so"))
    # ctypes.cdll.LoadLibrary(os.path.join(LIB_PATH, "libtorch_python.so"))
    # ctypes.cdll.LoadLibrary(os.path.join(LIB_PATH, "libtorchbind_test.so"))
    # ... e assim por diante, se houver mais .so que o PyTorch exija
except OSError as e:
    # Se quiser, você pode tratar o erro aqui de forma mais amigável
    raise ImportError(f"Não foi possível carregar libtorch: {e}")

# Só agora importamos o módulo compilado,
# que depende de libtorch.so etc.

from .purecpp_chunks_clean import *
