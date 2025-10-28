import os 
from files import *
import random 


def clear_screen2():
    os.system('cls' if os.name == 'nt' else 'clear')



def clear_screen():
    print('\033c', end='')


def id_gen():
    """Gera um ID com 5 dígitos únicos e aleatórios."""
    # Cria lista com números de 0 a 9
    numbers = list(range(10))
    # Embaralha a lista
    random.shuffle(numbers)
    # Pega os primeiros 5 números
    random_list = numbers[:5]
    # Junta os números em uma string
    return ''.join(map(str, random_list))

# Remover chamada de test
    
    

a = id_gen()

print(a)