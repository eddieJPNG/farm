from files import load_json, save_json



def register_input():
    inputs = load_json("inputs.json")
    
    print('=== Cadastro de Insumo ===')
    input_id = input('ID do insumo (ex: I001): ')
    name = input('Nome do insumo: ')
    quantity = float(input('Quantidade: '))
    unit = input('Unidade de medida (kg, L, saco, dose): ')
    
    print("\nCategorias disponíveis:")
    print("1. Ração (feed)")
    print("2. Semente (seed)")
    print("3. Fertilizante (fertilizer)")
    print("4. Medicamento (medicine)")
    
    category_map = {
        "1": "ração",
        "2": "semente",
        "3": "fertilizante",
        "4": "medicamento"
    }
    
    category_option = input("Escolha a categoria (1-4): ")

    category = category_map.get(category_option, "outro")

    new_input = {
        'id': input_id,
        'name': name,
        'quantity': quantity,
        'unit': unit,
        'category': category
    }

    inputs.append(new_input)
    save_json("inputs.json", inputs)
    print('Insumo cadastrado com sucesso!')

def list_inputs():
    inputs = load_json("inputs.json")

    if len(inputs) == 0:
        print('Nenhum insumo cadastrado.')
        return

    print('=== Lista de Insumos ===')
    for item in inputs:
        print(f"ID: {item.get('id', '<sem id>')}, "
              f"Nome: {item.get('name', '<sem nome>')}, "
              f"Quantidade: {item.get('quantity', 0)} {item.get('unit', 'un')}, "
              f"Categoria: {item.get('category', '<sem categoria>')}")

def update_stock():
    inputs = load_json("inputs.json")
    input_id = input('Digite o ID do insumo: ')
    
    for item in inputs:
        if item['id'] == input_id:
            print(f"\nEstoque atual: {item['quantity']} {item['unit']}")
            operation = input('Operação (entrada/saída): ').lower()
            
            try:
                amount = float(input(f'Quantidade em {item["unit"]}: '))
                
                if operation == 'entrada':
                    item['quantity'] += amount
                    save_json(inputs)
                    print('Entrada registrada com sucesso!')
                    
                elif operation == 'saída':
                    if amount <= item['quantity']:
                        item['quantity'] -= amount
                        save_json("inputs.json", inputs)
                        print('Saída registrada com sucesso!')
                    else:
                        print('ERRO: Quantidade insuficiente em estoque!')
                else:
                    print('Operação inválida!')
                return
            except ValueError:
                print('ERRO: Digite um número válido!')
                return
                
    print('Insumo não encontrado!')

def search_input():
    inputs = load_json("inputs.json")
    input_id = input('Digite o ID do insumo: ')

    for item in inputs:
        if item['id'] == input_id:
            print('=== Insumo Encontrado ===')
            print(f'ID: {item["id"]}')
            print(f'Nome: {item["name"]}')
            print(f'Quantidade: {item["quantity"]} {item["unit"]}')
            print(f'Categoria: {item["category"]}')
            return

    print('Insumo não encontrado!')

def inputs_menu():
    """Menu principal do módulo de insumos."""
    while True:
        print("\n=== MENU INSUMOS ===")
        print("1. Cadastrar insumo")
        print("2. Listar insumos")
        print("3. Buscar insumo")
        print("4. Atualizar estoque")
        print("0. Voltar ao menu principal")

        option = input("Escolha uma opção: ")

        match option:
            case "1":
                register_input()
            case "2":
                list_inputs()
            case "3":
                search_input()
            case "4":
                update_stock()
            case "0":
                break
            case _:
                print("Opção inválida!")
                input("Pressione ENTER para continuar...")