from utils import  *
from files import  *
from animals import  *
from inputs import  *
from plants import  *
from reports import  *
from movements import  *





def menu():
    while True:
        clear_screen()

        
        print("\n")
        print("\nSISTEMA DE FAZENDA DIGITAL EM  PHYTON")
        print("1.Animais")
        print("2.Plantações")
        print("3.Insumos")
        print("4.Movimentos")
        print("5.Relatórios")
        print("0.Sair")

        option = input("Escolha uma das opções: ")

        match option:
            case "1":
                animals_menu()
            case "2":
                plants_menu()
            case "3":
                inputs_menu()
            case "4":
                movements_menu()
            case "5":
                reports_menu()
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida!")
        



    

        



        # if option == "1":
        #     animals_menu()
        # elif option == "2":
        #     plants_menu()
        # elif option == "3":
        #     inputs_menu()
        # elif option == "4":
        #     moviments_menu()
        # elif option == "5":
        #     reports_menu()
        # elif option == "0":
        #     print("Saindo...")
            
           
        #     break
        # else:
            # print("Opção invalida!")
            # input("Pressione ENTER para tentar novamente!")
           
if __name__ == "__main__":
    menu()

option = input()

