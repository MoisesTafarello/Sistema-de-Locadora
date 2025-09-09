# Criando a Classe Item

class Item:
    def __init__(self, codigo, titulo):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__disponivel = True

# Método Alugar e Devolver

    def alugar (self):
        if self.__disponivel:
            self.__disponivel = False
            print (f"{self.__titulo} foi alugado!")
        else:
            print (f"{self.__titulo} não está disponível no momento!")

    def devolver (self):
        if not self.__disponivel:
            self.__disponivel = True
            print (f"{self.__titulo} foi devolvido!")
        else:
            print (f"{self.__titulo} já está disponível!")


# Criando a Classe Item

class Filme:
    def __init__(self, codigo, titulo, genero, duracao):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__genero = genero
        self.__duracao = duracao


# Criando a Classe Jogo

class Jogo:
    def __init__(self, codigo, titulo, plataforma, faixa_etaria):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__disponivel = True
        self.__plataforma = plataforma
        self.__faixa_etaria = faixa_etaria


# Criando a Classe Cliente 

class Cliente:
    def __init__(self, nome, cpf, itens_locados):
        self.__nome = nome
        self.__cpf = cpf
        self.__itens_locados = []
    
# Métodos Locar, Devolver e Listar Itens

    def Locar (self, item = Item):
        if item.disponivel:
            item.alugar ()
            self.itens_locados.append(item)
        else:
            print (f"{item.titulo} não está disponível para locação!")
    
    def Devolver (self,item = Item):
        if item in self.itens_locados:
            print(f"Itens locados por {self.nome}:")
            for i, item in enumerate (self.itensLocados, start=1):
                print(f"{i}. {item.titulo}")
        else:
            print(f"{self.nome} não possui itens locados no momento!")
    
    def Listar_Itens_Alocados (self):
        if self.itens_locados:
            print(f"Itens locados por {self.nome}:")
            for i, item in enumerate(self.itensLocados, start=1):
                print(f"{i}. {item.titulo}")
        else:
            print(f"{self.nome} não possui itens locados no momento!")


# Criando a Classe Locadora

class Locadora:
    def __init__(self):
        self.__clientes = []
        self.__itens = []
    
# Métodos Cadastrar Cliente, Cadastrar Item, Listar Clientes, Listar Itens

    def cadastrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} cadastrado com sucesso!")

    def cadastrar_item(self, item: Item):
        self.itens.append(item)
        print(f"Item {item.titulo} cadastrado com sucesso!")

    def listar_clientes(self):
        print("=== Clientes cadastrados ===")
        for i, cliente in enumerate(self.clientes, start=1):
            print(f"{i}. {cliente.nome} - CPF: {cliente.cpf}")

    def listar_itens(self):
        print("=== Itens disponíveis ===")
        for i, item in enumerate(self.itens, start=1):
            status = "Disponível" if item.disponivel else "Alugado"
            print(f"{i}. {item.titulo} ({status})")

            
