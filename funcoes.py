import os
from classes import *

def cadastrar_cliente(locadora):
    nome = input("Informe seu nome: ")
    cpf = int(input("Informe seu CPF: "))  
    locadora.cadastrar_cliente(Cliente(nome, cpf))
        
def cadastrar_item(locadora):
    print ("Escolha uma das opções abaixo:\n")
    print ("1 - Filme")
    print ("2 - Jogo")
    print ()
    tipo = int(input("Escolha a opção que deseja: "))
    print()
    codigo = int(input("Código: "))
    titulo = input("Título: ")

    
    if tipo == 1:
        genero = input("Gênero: ")
        duracao = int(input("Duração: "))
        locadora.cadastrar_item(Filme(codigo, titulo, genero, duracao))
    elif tipo == 2:
        plataforma = input("Plataforma: ")
        faixa = int(input("Faixa Etária: "))
        locadora.cadastrar_item(Jogo(codigo, titulo, plataforma, faixa))
    else:
        print("Tipo Inválido")


def locar_item(locadora):
    if not locadora.clientes or not locadora.itens:
        print("Não há clientes ou itens cadastrados")
        return

    locadora.listar_clientes()
    a = int(input("Escolha o número do cliente: ")) - 1
    print ()
    locadora.listar_itens()
    print ()
    b = int(input("Escolha o número do item: ")) - 1

    cliente = locadora.clientes[a]
    item = locadora.itens[b]
    cliente.locar(item)


def devolver_item(locadora):
    if not locadora.clientes:
        print("Não há clientes cadastrados")
        return

    locadora.listar_clientes()
    a = int(input("Escolha o número do cliente: ")) - 1
    cliente = locadora.clientes[a]
    print ()
    
    cliente.listar_itens()
    if not cliente.itens_locados:
        return

    b = int(input("Escolha o número do item que deseja devolver: ")) - 1
    item = cliente.itens_locados[b]
    cliente.devolver(item)