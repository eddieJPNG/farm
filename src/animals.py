from files import load_json, save_json

# ==============================================================
# Script: animals.py
# Descrição: Módulo para gerenciamento de animais da fazenda digital.
# Contém funções para cadastro, listagem, busca e atualização de animais.
# ==============================================================

def register_animal():
    """Cadastra um novo animal no sistema."""
    animals = load_json("animals.json")

    print('=== Cadastro de Animal ===')
    animal_id = input('ID do animal: ')
    species = input('Espécie (ex: bovino, caprino): ')
    age = float(input('Idade: '))
    weight = float(input('Peso (kg): '))
    status = input('Status (active, sold, dead): ')

    new_animal = {
        'id': animal_id,
        'species': species,
        'age': age,
        'weight': weight,
        'status': status
    }

    animals.append(new_animal)
    save_json("animals.json", animals)
    print('Animal cadastrado com sucesso!')

def list_animals():
    """Lista todos os animais cadastrados."""
    animals = load_json("animals.json")

    if not animals:
        print('Nenhum animal cadastrado.')
        return

    print('=== Lista de Animais ===')
    for animal in animals:
        print(f"ID: {animal['id']}, "
              f"Espécie: {animal['species']}, "
              f"Idade: {animal['age']}, "
              f"Peso: {animal['weight']}kg, "
              f"Status: {animal['status']}")

def search_animal():
    """Busca um animal pelo ID."""
    animals = load_json("animals.json")
    search_id = input('Digite o ID do animal: ')

    for animal in animals:
        if animal['id'] == search_id:
            print('=== Animal Encontrado ===')
            print(f"ID: {animal['id']}")
            print(f"Espécie: {animal['species']}")
            print(f"Idade: {animal['age']}")
            print(f"Peso: {animal['weight']}kg")
            print(f"Status: {animal['status']}")
            return

    print('Animal não encontrado.')

def update_status():
    """Atualiza o status de um animal específico."""
    animals = load_json("animals.json")
    search_id = input('Digite o ID do animal para atualizar: ')

    for animal in animals:
        if animal["id"] == search_id:
            new_status = input('Novo status (active, sold, dead): ')
            animal['status'] = new_status
            save_json("animals.json", animals)
            print('Status atualizado com sucesso!')
            return

    print('Animal não encontrado')

def animals_menu():
    """Menu principal do módulo de animais."""
    while True:
        print("\n=== MENU ANIMAIS ===")
        print("1. Cadastrar animal")
        print("2. Listar animais")
        print("3. Buscar animal")
        print("4. Atualizar status")
        print("0. Voltar ao menu principal")

        option = input("Escolha uma opção: ")

        match option:
            case "1":
                register_animal()
            case "2":
                list_animals()
            case "3":
                search_animal()
            case "4":
                update_status()
            case "0":
                break
            case _:
                print("Opção inválida!")