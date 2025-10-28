from files import load_json, save_json
from datetime import datetime

def movements_menu():
    while True:
        print("\nMENU MOVIMENTAÇÕES")
        print("1. Registrar movimentações")
        print("2. Listar movimentações")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            register_movement()
        elif choice == "2":
            list_movements()
        elif choice == "3":
            break
        else:
            print("Opção inválida")

def register_movement():
    try:
        data = load_json("movements.json")

        type_m = input("Tipo (Venda/Colheita/Consumo): ")
        description = input("Descrição: ")
        value = input("Valor ou Quantidade: ")

        movement = {
            "type": type_m,
            "description": description,
            "value": value,
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        data.append(movement)
        save_json("movements.json", data)

        print("✅ Movimentação foi registrada com sucesso!")

    except Exception as e:
        print(f"Erro durante o registro de uma movimentação: {e}")

def list_movements():
    try:
        data = load_json("movements.json")

        if not data:
            print("Sem movimentações no momento.")
            return

        print("\n--- MOVEMENTS ---")
        for m in data:
            print(f"{m['date']} - {m['type']}: {m['description']} ({m['value']})")

    except Exception as e:
        print(f"Erro durante a listagem de uma movimentação: {e}")
