from random import random, shuffle
"""a = list(range(2))
print ("a - %s" %a)
b = list (range(2))
print ("b - %s" %b)
c = list(a)
c += list(b)
c += list(range(3))
print ("c - %s" %c)

print ("{} {} {}".format(a,b,c))"""

def quicksort(lista):
    if len(lista) <= 1: 
        return lista
    
    pivô = lista[0]
    iguais  = [x for x in lista if x == pivô]
    menores = [x for x in lista if x <  pivô]
    maiores = [x for x in lista if x >  pivô]
    return quicksort(menores) + iguais + quicksort(maiores)

#print (quicksort([2, 7, 0, 3, 4, 9, 8, 1, 5, 6]))


r = 100
lista_aux = list(range(r))

print(quicksort(lista_aux))