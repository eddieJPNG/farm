import json  # biblioteca para trabalhar com filess JSON
import os    # biblioteca para verificar se filess ou pastas existem

# verifica se a pasta "data" existe; se não, cria
if not os.path.exists("data"):
    os.mkdir("data")

def load_json(filename):
    # tenta abrir o files; se não existir, cria um vazio
    if not os.path.exists(filename):
        with open(filename, "w") as files:
            json.dump([], files)  # cria o files e coloca uma lista vazia

    # abre o files para leitura
    with open(filename, "r") as files:
        data = json.load(files)  # lê o conteúdo JSON e transforma em lista/dicionário

    return data  # devolve os data lidos

def save_json(filename, data):
    # abre o files para escrita (vai substituir o conteúdo antigo)
    with open(filename, "w") as files:
        json.dump(data, files)  # salva os data no formato JSON
