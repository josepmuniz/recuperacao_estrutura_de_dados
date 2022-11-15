from celulas import Celula


class Pilhas:
    def __int__(self):
        self.__total_de_variaveis = 0
        self.__primeiro = None
        self.__pecas = self.__total_de_variaveis



    #def __str__(self):
     #   variavel = '{}''[]''()'
      # return string

   # def variavel(self):

    #    variavel = 0
     #   return variavel

    def variavel(self):
      return self.__total_de_variaveis

    def adiciona_comeco(self, variavel):
        nova_celula = Celula(self.__primeiro, variavel)
        self.__primeiro = nova_celula

        if self.__total_de_variaveis == 0:
            self.__ultima = self.__primeiro

        self.__total_de_variaveis += 1

    def insere(self, variavel):
        self.__primeiro(variavel)

    def condicao(self):
        if self.__total_de_variaveis != 0:
            return False
        return True

    def elemento(self):
        s = ""
        t = ""
        self.__total_de_variaveis = s
        self.__total_de_variaveis = t


        if "#" is not None:
            return False
        return True


    def contem(self, variavel):
        atual = self.__primeiro

        while atual is not None:
            if atual.variavel == variavel:
                return True
            atual = atual.proxima
        return False

    def __str__(self):

        if self.__total_de_variaveis == 0:
            return ''

        string_final = ''
        atual = self.__primeiro

        for i in range(0, self.__total_de_variaveis-1):
            string_final = string_final + atual.elemento
            string_final = string_final + ', '
            atual = atual.proxima


        string_final = string_final + atual.variavel
        string_final = string_final +''
        return string_final










