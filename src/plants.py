from files import *

def plants_menu():
    while True:
        print("\n🌱 MENU DE PLANTAÇÕES")
        print("1. Registrar plantação")
        print("2. Listar plantações")
        print("3. Voltar")
        op = input("Escolha: ")
        if op == "1":
            cadastrar_planta()
        elif op == "2":
            listar_plantas()
        elif op == "3":
            break


def cadastrar_planta():
    data = load_json("plants.json")
    tipo = input("Tipo de planta: ")
    area = input("Área (hectares): ")
    data.append({"tipo": tipo, "area": area})
    save_json("plants.json", data)
    print("✅ Plantação registrada!")

def listar_plantas():
    data = load_json("plants.json")
    if not data:
        print("Nenhuma plantação registrada.")
    else:
        for p in data:
            print(f"- {p['tipo']} ({p['area']} ha)")
