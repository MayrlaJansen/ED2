from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *
import random
import datetime
'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''

if __name__ == "__main__":
    print("Informe qual Algoritmo de Ordenaçao deseja usar:")

    escolha = input("1 - QuickSort\n2 - MergeSort\n3 - InsertionSort\n4 - Quicksort + Inserção Parcial\n"
                "5 - Quicksort + Inserção Final\n6 - Mergesort + Inserção Parcial\n7 - Mergesort + Inserção Final\n")
    if int(escolha) == 1:
        algoritimoDeOrdenacao = QuickSort()
    elif int(escolha) == 2:
        algoritimoDeOrdenacao = MergeSort()
    elif int(escolha) == 3:
        algoritimoDeOrdenacao = InsertionSort()
    elif int(escolha) == 4:
        algoritimoDeOrdenacao = QuicksortInsercaoParcial()
    elif int(escolha) == 5:
        algoritimoDeOrdenacao = QuicksortInsercaoFinal()
    elif int(escolha) == 6:
        algoritimoDeOrdenacao = MergesortInsercaoParcial()
    elif int(escolha) == 7:
        algoritimoDeOrdenacao = MergesortInsercaoFinal()
    else:
        print("Entrada Invalida!")
        quit()


    print("Informe qual arquivo de Vertices deseja usar:")
    vertices = input("1 - 7 vertices\n2 - 100 vertices\n3 - 1000 vertices\n4 - 10000 vertices\n5 - 100000 vertices\n")
    if int(vertices) == 1:
        arquivoJson = '../grafos/7vertices.json'

    elif int(vertices) == 2:
        arquivoJson = '../grafos/100vertices.json' 

    elif int(vertices) == 3:
        arquivoJson = '../grafos/1000vertices.json'

    elif int(vertices) == 4:
        arquivoJson = '../grafos/10000vertices.json'
      
    elif int(vertices) == 5:
        arquivoJson = '../grafos/100000vertices.json'

    else:
        print("Nenhum tamanho de entrada apresentado foi selecionado")
        
    
    
    
    arq = str(random.randint(1,100000))
    arquivoDeSaida = '../arvores_geradas/tree'+arq+'Vertices.txt' 
    
    # algoritimoDeOrdenacao = InsertionSort()
    # arquivoJson = '../grafos/7vertices.json'
    
    inicio = datetime.datetime.now()

    grafo = Grafo()
    grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
    grafo.carregarGrafo(arquivoJson)

    arvoreGeradoraMinima =  grafo.executarKruskal() 
    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)

    print ("nome do arquivo gerado:",arquivoDeSaida)
    fim = datetime.datetime.now()

    tempo = fim- inicio

    print ("tempo total de execucao do algoritmo:", tempo) 

