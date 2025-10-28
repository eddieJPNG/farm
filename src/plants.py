from files import load_json, save_json
from datetime import datetime, timedelta

def calculate_harvest_date(crop_type, planting_date):
    """Calcula a data estimada de colheita baseada no tipo de cultura"""
    try:
        planting_date = datetime.strptime(planting_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida. Use o formato YYYY-MM-DD")
    
    harvest_periods = {
        "milho": 120,  # 4 meses
        "soja": 150,   # 5 meses
        "arroz": 120,  # 4 meses
        "hortaliça": 90 # 3 meses
    }
    
    days = harvest_periods.get(crop_type.lower(), 120)
    harvest_date = planting_date + timedelta(days=days)
    return harvest_date.strftime("%Y-%m-%d")

def register_plantation():
    plants = load_json("plants.json")
    
    print('=== Cadastro de Plantação ===')
    plant_id = input('ID da plantação (ex: P001): ')
    crop_type = input('Tipo de cultura (milho, soja, arroz, hortaliça): ')
    area = float(input('Área cultivada (hectares): '))
    planting_date = input('Data de plantio (YYYY-MM-DD): ')
    
    harvest_date = calculate_harvest_date(crop_type, planting_date)
    
    new_plantation = {
        'id': plant_id,
        'crop_type': crop_type,
        'area': area,
        'planting_date': planting_date,
        'harvest_date': harvest_date,
        'status': 'planted'
    }
    
    plants.append(new_plantation)
    save_json("plants.json", plants)
    print('Plantação cadastrada com sucesso!')

def list_plantations():
    plants = load_json("plants.json")
    
    if len(plants) == 0:
        print('Nenhuma plantação cadastrada.')
        return
        
    print('=== Lista de Plantações ===')
    
    for plant in plants:
        print(f'ID: {plant["id"]}, Cultura: {plant["crop_type"]}, '
              f'Área: {plant["area"]}ha, Plantio: {plant["planting_date"]}, '
              f'Colheita Prevista: {plant["harvest_date"]}, Status: {plant["status"]}')

def search_plantation():
    plants = load_json("plants.json")
    search_id = input('Digite o ID da plantação: ')
    
    for plant in plants:
        if plant['id'] == search_id:
            print('=== Plantação Encontrada ===')
            print(f'ID: {plant["id"]}')
            print(f'Cultura: {plant["crop_type"]}')
            print(f'Área: {plant["area"]} hectares')
            print(f'Data de Plantio: {plant["planting_date"]}')
            print(f'Previsão de Colheita: {plant["harvest_date"]}')
            print(f'Status: {plant["status"]}')
            return
            
    print('Plantação não encontrada.')

def update_plantation_status():
    plants = load_json("plants.json")
    search_id = input('Digite o ID da plantação para atualizar: ')
    
    for plant in plants:
        if plant['id'] == search_id:
            print('Status disponíveis: plantado, colhido, rotacionado, inativo')
            new_status = input('Novo status: ')
            if new_status in ["plantado", "colhido", "rotacionado", "inativo"]:
                plant['status'] = new_status
                save_json("plants.json", plants)
                print('Status atualizado com sucesso!')
            else:
                print('Status inválido!')
            return
            
    print('Plantação não encontrada.')

def plants_menu():
    """Menu principal do módulo de plantações."""
    while True:
        print("\n=== MENU PLANTAÇÕES ===")
        print("1. Cadastrar plantação")
        print("2. Listar plantações")
        print("3. Buscar plantação")
        print("4. Atualizar status")
        print("0. Voltar ao menu principal")
        
        option = input("Escolha uma opção: ")
        
        match option:
            case "1":
                register_plantation()
            case "2":
                list_plantations()
            case "3":
                search_plantation()
            case "4":
                update_plantation_status()
            case "0":
                break
            case _:
                print("Opção inválida!")
                input("Pressione ENTER para continuar...")