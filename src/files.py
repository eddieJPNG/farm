import json
import os

# ==============================================================
# Script: files.py
# Descrição: Este arquivo faz parte do sistema de controle da fazenda.
# Ele contém funções e classes para gerenciar entidades e operações específicas.
# ==============================================================

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data")

def load_json(filename):
    """Carrega dados de um arquivo JSON."""
    path = os.path.join(DATA_PATH, filename)
    
    try:
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Erro ao ler {filename}. Iniciando com lista vazia.")
        return []
    except OSError as e:
        print(f"Erro de I/O ao ler {filename}: {e}")
        return []

def save_json(filename, data):
    """Salva dados em um arquivo JSON."""
    try:
        # Garante que o diretório data existe
        if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)
            
        path = os.path.join(DATA_PATH, filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except OSError as e:
        print(f"Erro ao salvar {filename}: {e}")

# Remova ou comente o código de teste abaixo
# d = {
#     "b": "Oi",
#     "a": "hey",
# }
# save_json("plants.json", d)
# print(load_json("plants.json"))