from files import load_json, save_json
from datetime import datetime

def movements_menu():
    while True:
        print("\nMOVEMENTS MENU")
        print("1. Register movement")
        print("2. List movements")
        print("3. Back")

        choice = input("Choose: ")

        if choice == "1":
            register_movement()
        elif choice == "2":
            list_movements()
        elif choice == "3":
            break
        else:
            print("Invalid option.")

def register_movement():
    try:
        data = load_json("movements.json")

        type_m = input("Type (Sale/Harvest/Consume): ")
        description = input("Description: ")
        value = input("Value or quantity: ")

        movement = {
            "type": type_m,
            "description": description,
            "value": value,
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        data.append(movement)
        save_json("movements.json", data)

        print("✅ Movement registered successfully.")

    except Exception as e:
        print(f"Error while registering movement: {e}")

def list_movements():
    try:
        data = load_json("movements.json")

        if not data:
            print("No movements registered.")
            return

        print("\n--- MOVEMENTS ---")
        for m in data:
            print(f"{m['date']} - {m['type']}: {m['description']} ({m['value']})")

    except Exception as e:
        print(f"Error while listing movements: {e}")
