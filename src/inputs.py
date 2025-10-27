from files import *

def inputs_menu():
    while True:
        print("\n🧪 MENU DE INSUMOS")
        print("1. Adicionar insumo")
        print("2. Listar insumos")
        print("3. Voltar")
        op = input("Escolha: ")
        if op == "1":
            cadastrar_insumo()
        elif op == "2":
            listar_insumos()
        elif op == "3":
            break

def cadastrar_insumo():
    data = load_json("inputs.json")
    nome = input("Nome do insumo: ")
    qtd = int(input("Quantidade: "))
    data.append({"nome": nome, "quantidade": qtd})
    save_json("inputs.json", data)
    print("✅ Insumo adicionado!")

def listar_insumos():
    data = load_json("inputs.json")
    if not data:
        print("Nenhum insumo cadastrado.")
    else:
        for i in data:
            print(f"- {i['nome']}: {i['quantidade']} unidades")
