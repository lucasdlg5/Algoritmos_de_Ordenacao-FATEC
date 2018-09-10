#Lucas Domingos Leão Gomes

def selection(v):
    ordenado = []
    while v:
        ordenado.append(min(v)) #Procura o menor valor do array e adiciona ao vetor auxiliar ORDENADO
        v.remove(min(v)) #Captura a mesma referencia do menor valor da variavel V e o remove
    return ordenado
    
def mergesort():

    return 0

def quicksort():
    
    return 0


from random import random, shuffle
lista = list(range(20))
shuffle(lista)
print(selection(lista))