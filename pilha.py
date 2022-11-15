class Pilhas:

    def variavel(self, s):
      pilha = []
      for i in s:
        if i =='(' or i =='[' or i == '{':
          pilha.append(i)
        else:
          topo = pilha[-1]
          if ( i == ")" and topo == "(" ) or ( i == "]" and topo == "[" ) or ( i == "}" and topo == "{" ):
            pilha.pop()
          else:
            return False
      if len(pilha) == 0:
        return True
      else:
        return False



