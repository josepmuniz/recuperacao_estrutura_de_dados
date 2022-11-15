from celulas import Celula

class ListaLigada_Especial_Pilha:

    def __init__(self):
        self.__primeiro = None
        self.__total_de_elementos = 0


    def adiciona_comeco(self, elemento):
        nova_celula = Celula(self.__primeiro, elemento)
        self.__primeiro = nova_celula

        if self.__total_de_elementos == 0:
            self.__ultima = self.__primeiro

        self.__total_de_elementos += 1

    def adiciona_fim(self, elemento):
        if self.__total_de_elementos == 0:
            self.adiciona_comeco(elemento)
        else:
            nova_celula = Celula(None, elemento)
            self.__ultima.proxima = nova_celula
            self.__ultima = nova_celula
            self.__total_de_elementos +=1

    def adiciona_posicao(self, posicao, elemento):
        if posicao == 0:
            self.adiciona_comeco(elemento)
        elif posicao == self.__total_de_elementos:
            self.adiciona_fim(elemento)
        else:


            anterior = self.pega(posicao-1)

            nova = Celula(anterior.proxima, elemento)
            anterior.proxima = nova

            self.__total_de_elementos += 1

    def pega(self, posicao):




        atual = self.__primeiro

        for i in range(0, posicao):
            atual = atual.proxima
        return atual

    def remover_comeco(self):
        self.__primeiro = self.__primeiro.proxima

        self.__total_de_elementos -= 1


    def tamanho(self):
        return self.__total_de_elementos

    def contem(self, elemento):
        atual = self.__primeiro

        while atual is not None:
            if atual.elemento == elemento:
                return True
            atual = atual.proxima
        return False

    def __str__(self):

        if self.__total_de_elementos == 0:
            return '[]'

        string_final = '['
        atual = self.__primeiro

        for i in range(0, self.__total_de_elementos-1):
            string_final = string_final + atual.elemento
            string_final = string_final + ', '
            atual = atual.proxima


        string_final = string_final + atual.elemento
        string_final = string_final +']'
        return string_final
