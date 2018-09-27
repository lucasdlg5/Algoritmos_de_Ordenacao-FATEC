#Lucas Domingos Leão Gomes
from random import random, shuffle
import time, sys

sys.setrecursionlimit(999999999)
print ("-------------------------------------------------------------\n         |                         Time(s)                  |\n-------------------------------------------------------------\n         |    Mergesort    QuickSort     Selection    Native|")
def selection(v):
    ordenado = []
    while v:
        ordenado.append(min(v)) #Procura o menor valor do array e adiciona ao vetor auxiliar ORDENADO
        v.remove(min(v)) #Captura a mesma referencia do menor valor da variavel V e o remove
    return ordenado
    
def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)



"""def quicksort(lista):
    if len(lista) <= 1: 
        return lista
    
    pivô = lista[0]
    iguais  = [x for x in lista if x == pivô]
    menores = [x for x in lista if x <  pivô]
    maiores = [x for x in lista if x >  pivô]
    return quicksort(menores) + iguais + quicksort(maiores)"""


def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

def quicksort(myList, start, end):
    if start < end: 
        split = partition(myList, start, end)
        quicksort(myList, start, split-1)
        quicksort(myList, split+1, end)
    return myList


tempo = 0.0
r = 2000
lista_aux = list(range(r))
shuffle(lista_aux)
lista = []


while (tempo < 30.00):
    
    lista_aux = list (range(r))
    lista += (list(lista_aux))
    tempo_inicio = time.time()

    mergesort(list(lista))
    tempo = (time.time() - tempo_inicio)
    merge_tempo = "%.2f" % tempo
 
    tempo_inicio = time.time()
    quicksort(list(lista),0,len(lista)-1)
    tempo = (time.time() - tempo_inicio)
    quicksort_tempo =  "%.2f" % tempo  
    
    tempo_inicio = time.time()
    sorted(list(lista))
    tempo = (time.time() - tempo_inicio)
    native_tempo =   "%.2f" % tempo

    tempo_inicio = time.time()
    selection(list(lista))
    tempo = (time.time() - tempo_inicio)
    selection_tempo =   "%.2f" % tempo

    
    if (r < 9999):
        print ("{}     |    {}         {}           {}         {}".format(r, merge_tempo, quicksort_tempo, selection_tempo, native_tempo))
    else:
        print ("{}    |    {}         {}           {}        {}".format(r, merge_tempo, quicksort_tempo, selection_tempo, native_tempo))
    r += 2000
print ("-------------------------------------------------------------")
