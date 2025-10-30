from files import load_json, save_json
from datetime import datetime

def movements_menu():
    while True:
        print("\nMENU DE MOVIMENTAÇÕES")
        print("1. Registrar movimentação")
        print("2. Listar movimentações")
        print("0. Voltar")

        option = input("Escolha uma opção: ")

        match option:
            case "1":
                register_movement()
            case "2":
                list_movements()
            case "0":
                break
            case _:
                print("Opção inválida!")
                input("Pressione ENTER para continuar...")

def register_movement():
    try:
        movements_data = load_json("movements.json")

        movement_type = input("Tipo (Venda/Colheita/Consumo): ")
        description = input("Descrição: ")
        amount = input("Valor ou quantidade: ")

        movement = {
            "type": movement_type,
            "description": description,
            "amount": amount,
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        movements_data.append(movement)
        save_json("movements.json", movements_data)

        print("✅ Movimentação registrada com sucesso!")

    except Exception as error:
        print(f"Erro ao registrar movimentação: {error}")

def list_movements():
    try:
        movements_data = load_json("movements.json")

        if not movements_data:
            print("Nenhuma movimentação registrada.")
            return

        print("\n--- LISTA DE MOVIMENTAÇÕES ---")
        for movement in movements_data:
            print(f"{movement['date']} - {movement['type']}: {movement['description']} ({movement['amount']})")

    except Exception as error:
        print(f"Erro ao listar movimentações: {error}")
