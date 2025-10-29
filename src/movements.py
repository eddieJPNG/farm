from files import *
from datetime import datetime, date, time, timedelta

def movements_menu():
    while True:
        print("\nMENU DE MOVIMENTAÇÕES")
        print("1. Registrar movimentação")
        print("2. Listar movimentações")
        print("3. Voltar")
        op = input("Escolha: ")

        match op:
            case "1":
                registrar_movimento()
            case "2":
                listar_movimentos()
            case "3":
                break
            case _:
                print("Opção inválida!")

def registrar_movimento():
    data = load_json("movements.json")
    tipo = input("Tipo (Venda/Colheita/Consumo): ")
    descricao = input("Descrição: ")
    valor = input("Valor ou quantidade: ")

    data_atual = str(datetime.now())
    data.append({
        "tipo": tipo,
        "descricao": descricao,
        "valor": valor,
        "data": data_atual,
    })

    save_json("movements.json", data)
    print("✅ Movimentação registrada!")

def listar_movimentos():
    data = load_json("movements.json")
    if not data:
        print("Nenhuma movimentação registrada.")
    else:
        for m in data:
            print(f"- {m['tipo']}: {m['descricao']} ({m['valor']})")
