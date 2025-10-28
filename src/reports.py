# ==============================================================
# Script: reports.py
# Descrição: Gera relatórios gerais da fazenda e permite pesquisa.
# ==============================================================
import datetime
from files import *

# ===============================
# Função: Gerar Relatório Geral
# ===============================
def generate_report():
    print("\n📊 RELATÓRIO GERAL DA FAZENDA")

    reports = load_json("reports.txt")

    # Carregar dados
    animals = load_json("animals.json")
    plants = load_json("plants.json")
    inputs_ = load_json("inputs.json")

    # Dicionário de dados
    data = {
        "Animais": animals,
        "Plantações": plants,
        "Insumos": inputs_
    }

    # Escolher critério de ordenação
    print("\nOrdenar por:")
    print("1. Nome/ID (A–Z)")
    print("2. Quantidade (decrescente)")
    print("3. Status")
    order_option = input("Escolha uma opção: ")

    # Ordenar registros
    for key, items in data.items():
        if not items:
            continue
        match order_option:
            case "1":
                if "id" in items[0]:
                    items.sort(key=lambda x: str(x.get("id", "")).lower())
            case "2":
                if "quantity" in items[0]:
                    items.sort(key=lambda x: x.get("quantity", 0), reverse=True)
            case "3":
                if "status" in items[0]:
                    items.sort(key=lambda x: str(x.get("status", "")).lower())
        data[key] = items

    # Mostrar na tela
    for category, items in data.items():
        print(f"\n== {category} ==")
        if not items:
            print("Nenhum registro encontrado.")
        for item in items:
            print(item)

    # Gerar relatório JSON
    save_json("relatorio.json", data)

    # Gerar relatório TXT
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    total_animals = len(animals)
    total_plants = len(plants)
    total_inputs = len(inputs_)

    path = r"c:\Users\Creche Tia Matilde\Documents\github_repositories\farm\data\reports.txt"



    with open(path, "w", encoding="utf-8") as f:
        f.write("=== RELATÓRIO GERAL DA FAZENDA ===\n")
        f.write(f"Gerado em: {timestamp}\n\n")

        f.write(f"Total de Animais: {total_animals}\n")
        f.write(f"Total de Plantações: {total_plants}\n")
        f.write(f"Total de Insumos: {total_inputs}\n")
        f.write("\n----------------------------------------\n")

        for category, items in data.items():
            f.write(f"\n## {category} ##\n")
            if not items:
                f.write("Nenhum registro encontrado.\n")
                continue
            for item in items:
                f.write(str(item) + "\n")

    print("\n✅ Relatórios gerados com sucesso:")
    print("- data/relatorio.json")
    print("- data/report.txt")

# ===============================
# Função: Pesquisar Registros
# ===============================
def search_record():
    print("\n🔍 PESQUISA DE REGISTROS")
    query = input("Digite o ID ou nome a procurar: ").lower()

    databases = {
        "Animais": load_json("animals.json"),
        "Plantações": load_json("plants.json"),
        "Insumos": load_json("inputs.json")
    }

    found = False
    for category, records in databases.items():
        for item in records:
            if (str(item.get("id", "")).lower() == query or
                str(item.get("name", "")).lower() == query or
                str(item.get("species", "")).lower() == query):
                print(f"\n=== {category} ===")
                for k, v in item.items():
                    print(f"{k.capitalize()}: {v}")
                found = True

    if not found:
        print("Nenhum registro encontrado.")

# ===============================
# Menu principal do módulo
# ===============================
def reports_menu():
    while True:
        print("\n=== MENU RELATÓRIOS ===")
        print("1. Gerar relatório geral")
        print("2. Pesquisar registro")
        print("0. Voltar ao menu principal")

        option = input("Escolha uma opção: ")

        match option:
            case "1":
                generate_report()
            case "2":
                search_record()
            case "0":
                break
            case _:
                print("Opção inválida!")
