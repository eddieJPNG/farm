import os 
from files import *
import random 


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def id_gen():
    """Gera um ID com 5 dígitos únicos e aleatórios."""
    
    numbers = list(range(10))
   
    random.shuffle(numbers)
   
    random_list = numbers[:5]

    return ''.join(map(str, random_list))


    
    


