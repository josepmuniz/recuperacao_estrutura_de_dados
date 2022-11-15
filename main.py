#from pilha import Pilha
#from pilhas import Pilhas
#from especial_pilha import minPilha
from string_codificada import PilhaCod
def teste_pilha():

    #print('teste da função pilha')
    #pilha = Pilha()
    #pilha.insere('[]')
    #pilha.insere('()')
    #pilha.insere('{}')

    #print (pilha)

    #print('teste da função pilha')
    #pilha = Pilhas()
    #pilha.insere("ab#c")
    #pilha.insere("ad#c")
    #print(pilha.condicao())
    #pilha.insere("cd##")
    #pilha.insere("b")
    #print(pilha.condicao())


    #print('teste da função pilha')
    #pilha = minPilha()
    #pilha.push(2)
    #pilha.push(4)
    #pilha.top()
    #pilha.getMin()
    #pilha.pop()
    #pilha.push(-1)
    #pilha.getMin()

    #print(pilha)


    print('teste da função pilha')
    s = PilhaCod()
    s.codificador(s.insere("2[a]2[bc]"))
    print(s)








if __name__ == '__main__':
    teste_pilha()


