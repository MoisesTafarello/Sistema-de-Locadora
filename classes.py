class Item:
    def __init__(self, codigo, titulo):
        self.codigo = codigo
        self.titulo = titulo
        self.disponivel = True

    # Getters
    def get_codigo(self):
        return self.codigo

    def get_titulo(self):
        return self.titulo

    def get_disponivel(self):
        return self.disponivel

    # Setter
    def set_disponivel(self, valor):
        self.disponivel = valor

    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"{self.titulo} foi alugado!")
        else:
            print(f"{self.titulo} não está disponível no momento!")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"{self.titulo} foi devolvido!")
        else:
            print(f"{self.titulo} já está disponível!")


class Filme(Item):
    def __init__(self, codigo, titulo, genero, duracao):
        Item.__init__(self, codigo, titulo)
        self.genero = genero
        self.duracao = duracao


    def get_genero(self):
        return self.genero

    def get_duracao(self):
        return self.duracao


class Jogo(Item):
    def __init__(self, codigo, titulo, plataforma, faixa_etaria):
        Item.__init__(self, codigo, titulo)
        self.plataforma = plataforma
        self.faixa_etaria = faixa_etaria


    def get_plataforma(self):
        return self.plataforma

    def get_faixa_etaria(self):
        return self.faixa_etaria


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.itens_locados = []

    
    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_itens_locados(self):
        return self.itens_locados

    def locar(self, item):
        if item.disponivel:
            item.alugar()
            self.itens_locados.append(item)
        else:
            print(f"{item.titulo} não está disponível para locação!")

    def devolver(self, item):
        if item in self.itens_locados:
            item.devolver()
            self.itens_locados.remove(item)
        else:
            print(f"{self.nome} não possui este item para devolver!")

    def listar_itens(self):
        if self.itens_locados:
            print(f"Itens locados por {self.nome}:")
            for i, item in enumerate(self.itens_locados, start=1):
                print(f"{i}. {item.titulo}")
        else:
            print(f"{self.nome} não possui itens locados no momento!")


class Locadora:
    def __init__(self):
        self.clientes = []
        self.itens = []

    
    def get_clientes(self):
        return self.clientes

    def get_itens(self):
        return self.itens

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print ()
        print(f"Cliente {cliente.nome} cadastrado com sucesso!")

    def cadastrar_item(self, item):
        self.itens.append(item)
        print ()
        print(f"Item {item.titulo} cadastrado com sucesso!")

    def listar_clientes(self):
        if not self.clientes:
            print ("Nenhum cliente cadastrado")
        else:
            print("Clientes cadastrados")
            for i, cliente in enumerate(self.clientes, start=1):
                print(f"{i}. {cliente.nome} - CPF: {cliente.cpf}")

    def listar_itens(self):
        if not self.itens:
            print ("Nenhum item cadastrado")
        else:
            print("Itens disponíveis")
            for i, item in enumerate(self.itens, start=1):
                if item.disponivel:
                    status = ("Disponível")
                else:
                    status = ("Alugado")
                print(f"{i}. {item.titulo} ({status})")
