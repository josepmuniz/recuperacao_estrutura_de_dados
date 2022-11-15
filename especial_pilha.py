from ListaLigada_EspecialPilha import ListaLigada_Especial_Pilha

class minPilha:
    def __init__(self, elemento):
        self.__pecas = ListaLigada_Especial_Pilha()
        self.__pecas = elemento

    def insere(self, elemento):
        self.__pecas.adiciona_comeco(elemento)

    def push(self, elemento):
        self.__pecas.push(elemento)

    def pop(self):
        self.__pecas.pop()

    def top(self):
        self.__pecas.top()

    def getMin(self):
        self.__pecas.getMin()

    def remove(self):
        self.__pecas.remover_comeco()

    def vazia (self):
        if self.__pecas.tamanho() == 0:
            return True
        return False


    def __str__(self):
        return self.__pecas.__str__()