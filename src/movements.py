# ==============================================================
# Script: movements.py
# Descrição: Este arquivo faz parte do sistema de controle da fazenda.
# Ele contém funções e classes para gerenciar entidades e operações específicas.
# ==============================================================

# Importação de módulos necessários
from files import *
from datetime import datetime, date, time, timedelta


# Função responsável por: menu movimentos
def movements_menu():
    while True:
        print("\nMENU DE MOVIMENTAÇÕES")
        print("1. Registrar movimentação")
        print("2. Listar movimentações")
        print("3. Voltar")
        op = input("Escolha: ")
        if op == "1":
            registrar_movimento()
        elif op == "2":
            listar_movimentos()
        elif op == "3":
            break

# Função responsável por: registrar movimento
def registrar_movimento():
    data = load_json("movements.json")
    tipo = input("Tipo (Venda/Colheita/Consumo): ")
    descricao = input("Descrição: ")
    valor = input("Valor ou quantidade: ")

    data_atual = str(datetime.now())
    data.append({"tipo": tipo, "descricao": descricao, "valor": valor,"data": data_atual,})
    save_json("movements.json", data)
    print("✅ Movimentação registrada!")

# Função responsável por: listar movimentos
def listar_movimentos():
    data = load_json("movements.json")
    if not data:
        print("Nenhuma movimentação registrada.")
    else:
        for m in data:
            print(f"- {m['tipo']}: {m['descricao']} ({m['valor']})")
