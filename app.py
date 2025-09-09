import os
from classes import *
from funcoes import *

def menu ():
    locadora = Locadora ()

while True:
    try:
        os.system ("cls")
        print ("Sistema de Locadora")
        print ()
        print ("1 - Cadastrar Cliente")
        print ("2 - Cadastrar Item")
        print ("3 - Listar Clienetes")
        print ("4 - Listar Itens")
        print ("5 - Locar Item")
        print ("6 - Devolver Item")
        print ("7 - Sair")

        escolha = int(input("Coloque a opção que deseja prosseguir: "))

        match escolha:
            case 1:
                cadastrar_cliente(Locadora)
            
            case 2:
                cadastrar_item(Locadora)
            
            case 3:
                locadora.listar_clientes()

            case 4:
                locadora.listar_itens()

            case 5:
                locar_item(locadora)
            
            case 6:
                devolver_item(locadora)
            
            case 7:
                print("Saindo...")
                break
            case _:
                print("Opção inválida!")

    except Exception as e:
        print ("Ocorreu um erro inesperado. Faça novamente!")