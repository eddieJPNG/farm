import json  # biblioteca para trabalhar com arquivos JSON
import os    # biblioteca para verificar se arquivos ou pastas existem

# verifica se a pasta "data" existe; se não, cria
if not os.path.exists("data"):
    os.mkdir("data")

def ler_dados(caminho_arquivo):
    # tenta abrir o arquivo; se não existir, cria um vazio
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "w") as arquivo:
            json.dump([], arquivo)  # cria o arquivo e coloca uma lista vazia

    # abre o arquivo para leitura
    with open(caminho_arquivo, "r") as arquivo:
        dados = json.load(arquivo)  # lê o conteúdo JSON e transforma em lista/dicionário

    return dados  # devolve os dados lidos

def salvar_dados(caminho_arquivo, dados):
    # abre o arquivo para escrita (vai substituir o conteúdo antigo)
    with open(caminho_arquivo, "w") as arquivo:
        json.dump(dados, arquivo)  # salva os dados no formato JSON
