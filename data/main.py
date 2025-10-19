from files import ler_dados, salvar_dados  # importa as funções do outro arquivo

# Caminho do arquivo de teste
caminho = "data/teste.json"

# Lê os dados (se não existir, cria o arquivo)
dados = ler_dados(caminho)
print("Dados atuais:", dados)  # mostra o que tem dentro do arquivo

# Adiciona um novo item na lista de dados
novo_animal = {
    "id": 1,
    "especie": "Boi",
    "peso": 450,
    "idade": 2
}
dados.append(novo_animal)  # adiciona o animal à lista

# Salva os dados atualizados
salvar_dados(caminho, dados)
print("Novo animal salvo com sucesso!")
