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

def div_lista(array, ini_arr, fim_arr):
    p, d, ri, f_cod = array[ini_arr], ini_arr + 1, fim_arr, True
    while f_cod:
        while array[d] <= p and d <= ri:
            d += 1
        while ri >= d and array[ri] >= p:
            ri -= 1
        if ri < d:
            f_cod = False
        else:
            temp, array[d] = array[d], array[ri]
            array[ri] =  temp
    temp, array[ini_arr] = array[ini_arr], array[ri]
    array[ri] = temp
    return ri

def quicksort(array, ini_arr, fim_arr):
    if  fim_arr > ini_arr: 
        split = div_lista(array, ini_arr, fim_arr)
        quicksort(array, ini_arr, split-1)
        quicksort(array, split+1, fim_arr)
    return array


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
