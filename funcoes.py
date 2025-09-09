from classes import *

def cadastar_clientes (locadora):
    try:    
        nome =  input("Informe seu nome: ")
        cpf = int(input("Informe seu CPF: "))



    except Exception as e:
        print ("Ocorreu um erro inesperado. Faça novamente!")