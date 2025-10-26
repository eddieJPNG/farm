import json  # biblioteca para trabalhar com filess JSON
import os    # biblioteca para verificar se filess ou pastas existem

# ==============================================================
# Script: files.py
# Descrição: Este arquivo faz parte do sistema de controle da fazenda.
# Ele contém funções e classes para gerenciar entidades e operações específicas.
# ==============================================================



DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data")

# Função responsável por: load json
def load_json(filename):
    path = os.path.join(DATA_PATH, filename)
    try:
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Erro ao ler {filename}. Iniciando com lista vazia.")
        return []

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# Função responsável por: save json
def save_json(filename, data):
    path = os.path.join(DATA_PATH, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)



d = {
    "b": "Oi",
    "a": "hey",
}

save_json("plants.json", d)

print(load_json("plants.json"))