from files import load_json, save_json
from datetime import datetime

def movements_menu():
    while True:
        print("\nMOVEMENTS MENU")
        print("1. Register movement")
        print("2. List movements")
        print("3. Back")

        choice = input("Choose an option: ")

        match choice:
            case "1":
                register_movement()
            case "2":
                list_movements()
            case "3":
                break
            case _:
                print("Invalid option, try again.")

def register_movement():
    try:
        data = load_json("movements.json")

        mov_type = input("Type (Sale/Harvest/Consume): ")
        description = input("Description: ")
        value = input("Value or quantity: ")

        movement = {
            "type": mov_type,
            "description": description,
            "value": value,
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        data.append(movement)
        save_json("movements.json", data)

        print("✅ Movement registered successfully!")

    except Exception as e:
        print(f"Error registering movement: {e}")

def list_movements():
    try:
        data = load_json("movements.json")

        if not data:
            print("No movements registered.")
            return

        print("\n--- MOVEMENTS LIST ---")
        for m in data:
            print(f"{m['date']} - {m['type']}: {m['description']} ({m['value']})")

    except Exception as e:
        print(f"Error listing movements: {e}")
