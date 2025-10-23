import json  # para trabalhar com arquivos JSON

def read_movements():
    # tenta abrir o arquivo de movimentos e ler os dados
    try:
        file = open("data/movements.json", "r", encoding="utf-8")  # abre para leitura
        data = json.load(file)  # converte JSON em lista Python
        file.close()  # fecha o arquivo
        return data  # retorna a lista de movimentos
    except:
        # se ocorrer qualquer erro (arquivo não existir, ou conteúdo inválido),
        # retornamos uma lista vazia para o programa continuar funcionando
        return []

def save_movements(movements):
    # abre o arquivo para escrita e grava a lista de movimentos
    file = open("data/movements.json", "w", encoding="utf-8")
    json.dump(movements, file, ensure_ascii=False)  # escreve o JSON no arquivo
    file.close()  # fecha o arquivo

def add_movement(type, description, date):
    # lê os movimentos já existentes
    movements = read_movements()
    # cria um novo registro de movimentação
    new = {"type": type, "description": description, "date": date}
    # adiciona o novo registro à lista
    movements.append(new)
    # salva a lista atualizada de movimentos
    save_movements(movements)
    # confirma para o usuário que foi salvo
    print("Movement added successfully!")

def list_movements():
    # lê a lista de movimentos
    movements = read_movements()
    # verifica se há algo para mostrar
    if len(movements) == 0:
        print("No movements registered.")
    else:
        # percorre e imprime cada movimentação
        for m in movements:
            print(f"Type: {m['type']} | Description: {m['description']} | Date: {m['date']}")
