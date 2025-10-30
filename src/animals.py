from files import load_json, save_json
import json


def register_animal():
    animals = load_json("animals.json")

    print('=== Cadastro de Animal ===')
    animal_id = input('ID do animal: ')
    species = input('Espécie (ex: bovino, caprino): ')
    age = input('Idade: ')
    weight = input('Peso (kg): ')
    status = input('Status (Ativo, Vendido, Morto): ')

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
    animals = load_json("animals.json")

    if len(animals) == 0:
        print('Nenhum animal cadastrado.')
        return

    print('=== Lista de Animais ===')
    for animal in animals:
        print(f'ID: {animal['id']}, Espécie: {animal['species']}, Idade: {animal['age']}, Peso: {animal['weight']}kg, Status: {animal['status']}')

def search_animal():
    animals = load_json("animals.json")
    search_id = input('Digite o ID do animal: ')

    for animal in animals:
        if animal['id'] == search_id:
            print('=== Animal Encontrado ===\n')
            print(f'ID: {animal['id']}')
            print(f'Espécie: {animal['species']}')
            print(f'Idade: {animal['age']}')
            print(f'Peso: {animal['weight']}kg')
            print(f'Status: {animal['status']}')
            return

    print('Animal não encontrado.\n')

def update_status():
    animals = load_json("animals.json")
    search_id = input('Digite o ID do animal para atualizar: ')

    for animal in animals:
        if animal["id"] == search_id:
            new_status = input('Novo status (Ativo, Vendido, Morto): ')
            animal['status'] = new_status
            save_json("animals.json", animal )
            print('Status atualizado com sucesso!')
            return

    print('Animal não encontrado')

def animals_menu():
    
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
                
