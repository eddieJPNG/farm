import json   # Biblioteca para ler e salvar dados em formato JSON
import os     # Biblioteca para lidar com arquivos e pastas

# Verifica se a pasta 'data' existe, se não existir cria
if not os.path.exists("data"):  
    os.mkdir("data")  

def ler_dados(caminho_arquivo):
    # Se o arquivo não existir, cria um arquivo vazio com uma lista
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "w") as arquivo:  
            json.dump([], arquivo)  # Cria o arquivo e coloca uma lista vazia

    # Abre o arquivo para leitura e pega os dados
    with open(caminho_arquivo, "r") as arquivo:  
        dados = json.load(arquivo)  # Lê o conteúdo JSON e transforma em lista/dicionário

    return dados  # Retorna os dados lidos


def salvar_dados(caminho_arquivo, dados):
    # Abre o arquivo para escrita e salva os dados
    with open(caminho_arquivo, "w") as arquivo:  
        json.dump(dados, arquivo, indent=4)  # Salva os dados de forma organizada (indentado)
