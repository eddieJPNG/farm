
# animals.py
# Cadastro simples de animais para uma fazenda digital

import json

# Caminho do arquivo onde os dados dos animais serão salvos
file_path = 'data/animals.json'

# Função para carregar os animais do arquivo
def load_animals():
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            animals = json.load(file)
    except:
        animals = []
    return animals

# Função para salvar os animais no arquivo
def save_animals(animals):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(animals, file, indent=4, ensure_ascii=False)

# Função para cadastrar um novo animal
def register_animal():
    animals = load_animals()

    print('=== Cadastro de Animal ===')
    animal_id = input('ID do animal: ')
    species = input('Espécie (ex: bovino, caprino): ')
    age = input('Idade: ')
    weight = input('Peso (kg): ')
    status = input('Status (active, sold, dead): ')

    new_animal = {
        'id': animal_id,
        'species': species,
        'age': age,
        'weight': weight,
        'status': status
    }

    animals.append(new_animal)
    save_animals(animals)
    print('Animal cadastrado com sucesso!')

# Função para listar todos os animais
def list_animals():
    animals = load_animals()

    if len(animals) == 0:
        print('Nenhum animal cadastrado.')
        return

    print('=== Lista de Animais ===')
    for animal in animals:
        print(f'ID: {animal['id']}, Espécie: {animal['species']}, Idade: {animal['age']}, Peso: {animal['weight']}kg, Status: {animal['status']}')

# Função para buscar um animal pelo ID
def search_animal():
    animals = load_animals()
    search_id = input('Digite o ID do animal: ')

    for animal in animals:
        if animal['id'] == search_id:
            print('=== Animal Encontrado ===')
            print(f'ID: {animal['id']}')
            print(f'Espécie: {animal['species']}')
            print(f'Idade: {animal['age']}')
            print(f'Peso: {animal['weight']}kg')
            print(f'Status: {animal['status']}')
            return

    print('Animal não encontrado.')

# Função para atualizar o status de um animal
def update_status():
    animals = load_animals()
    search_id = input('Digite o ID do animal para atualizar: ')

    for animal in animals:
        if animal["id"] == search_id:
            new_status = input('Novo status (active, sold, dead): ')
            animal['status'] = new_status
            save_animals(animals)
            print('Status atualizado com sucesso!')
            return

    print('Animal não encontrado')