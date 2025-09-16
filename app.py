import os
from classes import *
from funcoes import *

def menu():
    locadora = Locadora()  
    
    while True:
        try:
            os.system("cls")
            print("Sistema de Locadora")
            print()
            print("1 - Cadastrar Cliente")
            print("2 - Cadastrar Item")
            print("3 - Listar Clientes")
            print("4 - Listar Itens")
            print("5 - Locar Item")
            print("6 - Devolver Item")
            print("7 - Sair")
            print ()

            escolha = int(input("Coloque a opção que deseja prosseguir: "))

            match escolha:

                case 1:
                    os.system ("cls")
                    cadastrar_cliente(locadora)
                    os.system ("pause")

                case 2:
                    os.system ("cls")
                    cadastrar_item(locadora)
                    os.system ("pause")
                
                case 3:
                    os.system ("cls")
                    locadora.listar_clientes()
                    os.system("pause")

                case 4:
                    os.system ("cls")
                    locadora.listar_itens()
                    os.system("pause")

                case 5:
                    os.system ("cls")
                    locar_item(locadora)
                    os.system("pause")

                case 6:
                    os.system ("cls")
                    devolver_item(locadora)
                    os.system("pause")

                case 7:
                    os.system ("pause")
                    break
                
                case _:
                    print("Opção inválida!")
                    os.system("pause")

        except Exception as e:
            print("Ocorreu um erro inesperado. Faça novamente!")
            os.system("pause")
            os.system("cls")

menu ()
