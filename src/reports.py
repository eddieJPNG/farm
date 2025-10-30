from datetime import datetime
from files import load_json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data")
REPORT_FILE = os.path.join(DATA_PATH, "report.txt")


def reports_menu():
    while True:
        print("\n📊 MENU DE RELATÓRIOS")
        print("1. Relatório Geral")
        print("2. Relatório de Animais")
        print("3. Relatório de Plantações")
        print("4. Relatório de Insumos")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                generate_general_report()
            case "2":
                generate_animals_report()
            case "3":
                generate_plants_report()
            case "4":
                generate_inputs_report()
            case "0":
                break
            case _:
                print("Opção inválida!")
                input("Pressione ENTER para continuar...")
        
            
def generate_animals_report():
    animals = load_json("animals.json")
    if not animals:
        print("⚠️ Nenhum animal cadastrado.")
        return

    criterio = input("Ordenar por [1] ID ou [2] Espécie: ")
    if criterio == "2":
        animals.sort(key=lambda x: x.get("species", "").lower())
    else:
        animals.sort(key=lambda x: x.get("id", ""))

    print("\n🐄 RELATÓRIO DE ANIMAIS")
    print("-" * 50)
    for a in animals:
        print(f"ID: {a['id']} | Espécie: {a['species']} | "
              f"Peso: {a['weight']}kg | Idade: {a['age']} | Status: {a['status']}")

    total = len(animals)
    ativos = sum(1 for a in animals if a['status'] == 'active')
    vendidos = sum(1 for a in animals if a['status'] == 'sold')
    mortos = sum(1 for a in animals if a['status'] == 'dead')

    print(f"\nTotal: {total} | Ativos: {ativos} | Vendidos: {vendidos} | Mortos: {mortos}")
    save_report_to_file("Relatório de Animais", animals)


def generate_plants_report():
    plants = load_json("plants.json")
    if not plants:
        print("⚠️ Nenhuma plantação cadastrada.")
        return

    criterio = input("Ordenar por [1] ID ou [2] Tipo de cultura: ")
    if criterio == "2":
        plants.sort(key=lambda x: x.get("crop_type", "").lower())
    else:
        plants.sort(key=lambda x: x.get("id", ""))

    print("\n🌾 RELATÓRIO DE PLANTAÇÕES")
    print("-" * 50)
    for p in plants:
        print(f"ID: {p['id']} | Cultura: {p['crop_type']} | Área: {p['area']}ha | "
              f"Plantio: {p['planting_date']} | Colheita: {p['harvest_date']} | Status: {p['status']}")

    total = len(plants)
    plantadas = sum(1 for p in plants if p['status'] == 'planted')
    colhidas = sum(1 for p in plants if p['status'] == 'harvested')

    print(f"\nTotal: {total} | Plantadas: {plantadas} | Colhidas: {colhidas}")
    save_report_to_file("Relatório de Plantações", plants)


def generate_inputs_report():
    inputs = load_json("inputs.json")
    if not inputs:
        print("⚠️ Nenhum insumo registrado.")
        return

    criterio = input("Ordenar por [1] Nome ou [2] Quantidade: ")
    if criterio == "2":
        inputs.sort(key=lambda x: x.get("quantity", 0), reverse=True)
    else:
        inputs.sort(key=lambda x: x.get("name", "").lower())

    print("\n🧱 RELATÓRIO DE INSUMOS")
    print("-" * 50)
    for i in inputs:
        print(f"ID: {i['id']} | Nome: {i['name']} | "
              f"Qtd: {i['quantity']} {i['unit']} | Categoria: {i['category']}")

    total = len(inputs)
    print(f"\nTotal de insumos: {total}")
    save_report_to_file("Relatório de Insumos", inputs)


def generate_general_report():
    animals = load_json("animals.json")
    plants = load_json("plants.json")
    inputs = load_json("inputs.json")

    print("\n📋 RELATÓRIO GERAL DA FAZENDA")
    print("-" * 50)
    print(f"Animais cadastrados: {len(animals)}")
    print(f"Plantações registradas: {len(plants)}")
    print(f"Insumos disponíveis: {len(inputs)}")

    resumo = {
        "Total de Animais": len(animals),
        "Total de Plantações": len(plants),
        "Total de Insumos": len(inputs),
    }

    save_report_to_file("Relatório Geral da Fazenda", resumo)



def save_report_to_file(title, data):
    try:
        if not os.path.exists(DATA_PATH):
            os.makedirs(DATA_PATH)

        with open(REPORT_FILE, "a", encoding="utf-8") as f:
            f.write(f"\n{'=' * 60}\n")
            f.write(f"{title}\nGerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            f.write(f"{'=' * 60}\n")

            if isinstance(data, list):
                for item in data:
                    for chave, valor in item.items():
                        f.write(f"{chave}: {valor}\n")
                    f.write("-" * 40 + "\n")
            else:
                for chave, valor in data.items():
                    f.write(f"{chave}: {valor}\n")

            f.write("\n")
        print(f"✅ Relatório salvo com sucesso em: {REPORT_FILE}")
    except OSError as e:
        print(f"❌ Erro ao salvar relatório: {e}")


