from ListaLigada_EspecialPilha import ListaLigada_Especial_Pilha

class PilhaCod:
    def __init__(self, valor):
        self.__pecas = ListaLigada_Especial_Pilha()
        self.__pecas = valor

    def insere(self, valor):
        self.__pecas.adiciona_comeco(valor)

    def codificador(self, k):
        self.__k = k
        k = self.__k * self.__pecas
        return k

    def __str__(self):
        return self.__pecas.__str__()


