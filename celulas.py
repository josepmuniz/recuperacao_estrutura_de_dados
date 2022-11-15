class Celula:

    def __init__(self, proxima, celula):
        self.__proximo = proxima
        self.__variavel = celula

    @property
    def proximo(self):
        return self.__proximo

    @proximo.setter
    def proxima(self, proxima):
        self.__proximo = proxima

    @property
    def elemento(self):
        return self.__variavel

    def __str__(self):
        return self.__variavel


    