# Introdução:
# - Implementar algoritmo de ordenação que receba uma colecão
# - A coleção é uma lista de arestas
# - Para comparar o peso as arestas entre dois item da coleção basta usar a chave 'weight' (peso)
# Exemplos:
# - Modo convencional
# colecao[i] operador de comparacao colecao[j]
# colecao[i] < colecao[j]
# - Modo que você vai usar
# int(colecao[i]['weight']) operador de comparacao int(colecao[j]['weight'])
# int(colecao[i]['weight']) < int(colecao[j]['weight'])
# É nescessário converter o valor pra Interger no momento da comparação a fim de evitar erros
# '''
import random
import sys

# # Sua classe algoritmo de ordenação precisar ter um método ordenar
class InsertionSort(object):
    def ordenar(self, colecao):
        '''
        O método ordenar recebe uma colecão
        realiza ordenacão na colecão
        retorna colecão após ordenação
        '''
        for i in range(1, len(colecao)): #percorre da 2 posicao ate o final
            key = colecao[i] #representa o indice do laco a ser ordenado
            j = i-1 #usa-se para "excluir" a parte ja ordenada
            while j >=0 and int(key['weight']) < int(colecao[j]['weight']) : #faz as comparacoes da chave com a parte que ainda não foi ordenada
                colecao[j+1] = colecao[j] #caso seja menor, move para uma posicao a frente da posicao atual
                j -= 1 #decremento de j
            colecao[j+1] = key #realiza-se a troca final
        return colecao


class MergeSort(object):
    def ordenar(self, colecao):

        if len(colecao)>1: #testa se o tamanho da colecao e maior que 1
            mid = int(len(colecao)//2) #acha o meio da colecao
            lefthalf = colecao[:mid] #divide para o lado esquerdo
            righthalf = colecao[mid:] #divide para o lado direito

            #recursion
            ##caso o teste dê errado, alterar para "self.mergeSort(lefthalf)"
            self.ordenar(lefthalf) #chamada recursiva para o lado esquerdo
            self.ordenar(righthalf) #chamada recursiva para o lado direito


            i=0
            j=0
            k=0

            while i < len(lefthalf) and j < len(righthalf): #laco que vai do primeiro elemento ate o final das listas criadas
                if int(lefthalf[i]['weight']) < int(righthalf[j]['weight']): #teste de comparacao
                    colecao[k]=lefthalf[i] #caso o elemento da esquerda seja menor, coloca-o na posicao 0 da colecao
                    i=i+1 #incremento de i
                else:
                    colecao[k]=righthalf[j] #caso o elemento da direita seja menor, coloca-o na posicao 0 da colecao
                    j=j+1 #incremento de j
                k=k+1 #incremento de k

            while i < len(lefthalf): #atribuicao da lista ao final da colecao, caso o da direita termine e ainda tenha elementos na esquerda
                colecao[k]=lefthalf[i] 
                i=i+1
                k=k+1

            while j < len(righthalf):#atribuicao da lista ao final da colecao, caso o da esquerda termine e ainda tenha elementos na direita
                colecao[k]=righthalf[j]
                j=j+1
                k=k+1


        return colecao

   




class QuickSort(object):
    def ordenar(self,colecao):
        self.sort(colecao, 0, len(colecao)-1)

        return colecao

    def particao(self, colecao, ini, fim):
        pivo = colecao[fim-1]
        start = ini
        end = ini
        for i in range(ini, fim):
            if int(colecao[i]['weight']) > int(pivo['weight']):
                end += 1
            else:
                end += 1       
                start += 1
                colecao[i], colecao[start-1] = colecao[start-1], colecao[i]
        return start-1
        
    def sort(self, colecao, ini, fim):
        if ini < fim:
            pp = self.randparticao(colecao, ini, fim)
            # self.sort(colecao, ini, pp)
            # self.sort(colecao, pp+1,fim)
            try:
                self.sort (colecao, ini, pp)
            except RecursionError :
                sys.setrecursionlimit(3000) 
                self.sort (colecao, ini, pp)
            try:
                self.sort(colecao, pp+1, fim)
            except RecursionError :
                sys.setrecursionlimit(3000) 
                self.sort(colecao, pp+1, fim)

    def randparticao(self,colecao,ini,fim):
        rand = random.randrange(ini,fim)
        colecao[rand], colecao[fim-1] = colecao[fim-1], colecao[rand]
        return self.particao(colecao,ini,fim)
        
            

class QuicksortInsercaoParcial(object):
    def ordenar(self,colecao):
        L = input("Informe o L desejado:")
        print ("L escolhido:", L)
        self.sort(colecao, 0, len(colecao)-1, L)

        return colecao

    def particao(self, colecao, ini, fim):
        pivo = colecao[fim-1]
        start = ini
        end = ini
        for i in range(ini, fim):
            if int(colecao[i]['weight']) > int(pivo['weight']):
                end += 1
            else:
                end += 1       
                start += 1
                colecao[i], colecao[start-1] = colecao[start-1], colecao[i]
        return start-1
        
    def sort(self, colecao, ini, fim, L):
        if int(fim+1) <= int(L):
            for i in range(1, len(colecao)): #percorre da 2 posicao ate o final
                key = colecao[i] #representa o indice do laco a ser ordenado
                j = i-1 #usa-se para "excluir" a parte ja ordenada
                while j >=0 and int(key['weight']) < int(colecao[j]['weight']) : #faz as comparacoes da chave com a parte que ainda não foi ordenada
                    colecao[j+1] = colecao[j] #caso seja menor, move para uma posicao a frente da posicao atual
                    j -= 1 #decremento de j
                colecao[j+1] = key #realiza-se a troca final
            return colecao
        if ini < fim:
            pp = self.randparticao(colecao, ini, fim)
            self.sort(colecao, ini, pp, L)
            self.sort(colecao, pp+1,fim, L)
    
    def randparticao(self,colecao,ini,fim):
        rand = random.randrange(ini,fim)
        colecao[rand], colecao[fim-1] = colecao[fim-1], colecao[rand]
        return self.particao(colecao,ini,fim)







class QuicksortInsercaoFinal(object):
    def ordenar(self,colecao):
        L = input("Informe o L desejado:")
        print ("L escolhido:", L)
        self.sort(colecao, 0, len(colecao)-1, L)

        return colecao

    def particao(self, colecao, ini, fim):
        pivo = colecao[fim-1]
        start = ini
        end = ini
        for i in range(ini, fim):
            if int(colecao[i]['weight']) > int(pivo['weight']):
                end += 1
            else:
                end += 1       
                start += 1
                colecao[i], colecao[start-1] = colecao[start-1], colecao[i]
        return start-1
        
    def sort(self, colecao, ini, fim, L):
        if ini < fim:
            pp = self.randparticao(colecao, ini, fim)
            self.sort(colecao, ini, pp, L)
            self.sort(colecao, pp+1,fim, L)
            if (int(fim) <= int(L)) and (int(pp+1)<=int(L)):
                for i in range(1, len(colecao)): #percorre da 2 posicao ate o final
                    key = colecao[i] #representa o indice do laco a ser ordenado
                    j = i-1 #usa-se para "excluir" a parte ja ordenada
                    while j >=0 and int(key['weight']) < int(colecao[j]['weight']) : #faz as comparacoes da chave com a parte que ainda não foi ordenada
                        colecao[j+1] = colecao[j] #caso seja menor, move para uma posicao a frente da posicao atual
                        j -= 1 #decremento de j
                    colecao[j+1] = key #realiza-se a troca final
                return colecao
    
    def randparticao(self,colecao,ini,fim):
        rand = random.randrange(ini,fim)
        colecao[rand], colecao[fim-1] = colecao[fim-1], colecao[rand]
        return self.particao(colecao,ini,fim)





class MergesortInsercaoParcial(object):
    def ordenar(self, colecao):
        L = input("Informe o L:")
        print(L)
        self.func(colecao, L)
        return colecao
    def func(self,colecao, L):
        if len(colecao)>1: #testa se o tamanho da colecao e maior que 1
            mid = int(len(colecao)//2) #acha o meio da colecao
            lefthalf = colecao[:mid] #divide para o lado esquerdo
            righthalf = colecao[mid:] #divide para o lado direito

            #recursion
            ##caso o teste dê errado, alterar para "self.mergeSort(lefthalf)"
            
            if (len(lefthalf) <= int(L)) and (len(righthalf) <= int(L)):
                self.ordenarInsercao(lefthalf)
                self.ordenarInsercao(righthalf)


            else:
                self.func(lefthalf,L) #chamada recursiva para o lado esquerdo
                self.func(righthalf,L) #chamada recursiva para o lado direito


            i=0
            j=0
            k=0

            while i < len(lefthalf) and j < len(righthalf): #laco que vai do primeiro elemento ate o final das listas criadas
                if int(lefthalf[i]['weight']) < int(righthalf[j]['weight']): #teste de comparacao
                    colecao[k]=lefthalf[i] #caso o elemento da esquerda seja menor, coloca-o na posicao 0 da colecao
                    i=i+1 #incremento de i
                else:
                    colecao[k]=righthalf[j] #caso o elemento da direita seja menor, coloca-o na posicao 0 da colecao
                    j=j+1 #incremento de j
                k=k+1 #incremento de k

            while i < len(lefthalf): #atribuicao da lista ao final da colecao, caso o da direita termine e ainda tenha elementos na esquerda
                colecao[k]=lefthalf[i] 
                i=i+1
                k=k+1

            while j < len(righthalf):#atribuicao da lista ao final da colecao, caso o da esquerda termine e ainda tenha elementos na direita
                colecao[k]=righthalf[j]
                j=j+1
                k=k+1
        return colecao
        
    def ordenarInsercao(self, list):
        for i in range(1, len(list)): #percorre da 2 posicao ate o final
            key = list[i] #representa o indice do laco a ser ordenado
            j = i-1 #usa-se para "excluir" a parte ja ordenada
            while j >=0 and int(key['weight']) < int(list[j]['weight']) : #faz as comparacoes da chave com a parte que ainda não foi ordenada
                list[j+1] = list[j] #caso seja menor, move para uma posicao a frente da posicao atual
                j -= 1 #decremento de j
            list[j+1] = key #realiza-se a troca final
        return list
  
           



class MergesortInsercaoFinal(object):
    def ordenar(self, colecao):
        L = input("Informe o L:")
        print(L)
        self.func(colecao, L)
        for i in range(1, len(colecao)): #percorre da 2 posicao ate o final
            key = colecao[i] #representa o indice do laco a ser ordenado
            j = i-1 #usa-se para "excluir" a parte ja ordenada
            while j >=0 and int(key['weight']) < int(colecao[j]['weight']) : #faz as comparacoes da chave com a parte que ainda não foi ordenada
                colecao[j+1] = colecao[j] #caso seja menor, move para uma posicao a frente da posicao atual
                j -= 1 #decremento de j
            colecao[j+1] = key #realiza-se a troca final
        return colecao
    def func(self,colecao, L):
        if len(colecao)>1: #testa se o tamanho da colecao e maior que 1
            mid = int(len(colecao)//2) #acha o meio da colecao
            lefthalf = colecao[:mid] #divide para o lado esquerdo
            righthalf = colecao[mid:] #divide para o lado direito

            #recursion
            
            if (len(lefthalf) <= int(L)) and (len(righthalf) <= int(L)): #teste se as duas listas sao menores ou iguais a L
                # self.ordenarInsercao(lefthalf)
                # self.ordenarInsercao(righthalf)
                
                self.mesclar(lefthalf, righthalf, colecao)
                # self.ordenarInsercao(list)


            else:
                self.func(lefthalf,L) #chamada recursiva para o lado esquerdo
                self.func(righthalf,L) #chamada recursiva para o lado direito


            i=0
            j=0
            k=0

            while i < len(lefthalf) and j < len(righthalf): #laco que vai do primeiro elemento ate o final das listas criadas
                if int(lefthalf[i]['weight']) < int(righthalf[j]['weight']): #teste de comparacao
                    colecao[k]=lefthalf[i] #caso o elemento da esquerda seja menor, coloca-o na posicao 0 da colecao
                    i=i+1 #incremento de i
                else:
                    colecao[k]=righthalf[j] #caso o elemento da direita seja menor, coloca-o na posicao 0 da colecao
                    j=j+1 #incremento de j
                k=k+1 #incremento de k

            while i < len(lefthalf): #atribuicao da lista ao final da colecao, caso o da direita termine e ainda tenha elementos na esquerda
                colecao[k]=lefthalf[i] 
                i=i+1
                k=k+1

            while j < len(righthalf):#atribuicao da lista ao final da colecao, caso o da esquerda termine e ainda tenha elementos na direita
                colecao[k]=righthalf[j]
                j=j+1
                k=k+1
        return colecao
        
    # def ordenarInsercao(self, list):
    #     for i in range(1, len(list)): #percorre da 2 posicao ate o final
    #         key = list[i] #representa o indice do laco a ser ordenado
    #         j = i-1 #usa-se para "excluir" a parte ja ordenada
    #         while j >=0 and int(key['weight']) < int(list[j]['weight']) : #faz as comparacoes da chave com a parte que ainda não foi ordenada
    #             list[j+1] = list[j] #caso seja menor, move para uma posicao a frente da posicao atual
    #             j -= 1 #decremento de j
    #         list[j+1] = key #realiza-se a troca final
    #     return list
    
    def mesclar(self, lefthalf, righthalf,colecao):
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf): #laco que vai do primeiro elemento ate o final das listas criadas
                if int(lefthalf[i]['weight']) < int(righthalf[j]['weight']): #teste de comparacao
                    colecao[k]=lefthalf[i] #caso o elemento da esquerda seja menor, coloca-o na posicao 0 da colecao
                    i=i+1 #incremento de i
                else:
                    colecao[k]=righthalf[j] #caso o elemento da direita seja menor, coloca-o na posicao 0 da colecao
                    j=j+1 #incremento de j
                k=k+1 #incremento de k

        while i < len(lefthalf): #atribuicao da lista ao final da colecao, caso o da direita termine e ainda tenha elementos na esquerda
                colecao[k]=lefthalf[i] 
                i=i+1
                k=k+1

        while j < len(righthalf):#atribuicao da lista ao final da colecao, caso o da esquerda termine e ainda tenha elementos na direita
                colecao[k]=righthalf[j]
                j=j+1
                k=k+1

        # for i in range(1, len(colecao)): #percorre da 2 posicao ate o final
        #     key = colecao[i] #representa o indice do laco a ser ordenado
        #     j = i-1 #usa-se para "excluir" a parte ja ordenada
        #     while j >=0 and int(key['weight']) < int(colecao[j]['weight']) : #faz as comparacoes da chave com a parte que ainda não foi ordenada
        #         colecao[j+1] = colecao[j] #caso seja menor, move para uma posicao a frente da posicao atual
        #         j -= 1 #decremento de j
        #     colecao[j+1] = key #realiza-se a troca final
        return colecao
