import os 
from files import *
from main import *
from plants import *
from inputs import *
from animals import *
import random 


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_plant_id(data):
    # Gera ID no formato P001, P002... tenta respeitar IDs existentes (str ou int)
    max_n = 0
    for item in data:
        raw = item.get("id")
        if raw is None:
            continue
        s = str(raw)
        if s.upper().startswith("P"):
            try:
                n = int(s[1:])
            except:
                continue
        else:
            try:
                n = int(s)
            except:
                continue
        if n > max_n:
            max_n = n
    return f"P{max_n+1:03d}"




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