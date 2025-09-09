class Item:
    def __init__(self, codigo, titulo):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__disponivel = True

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


        