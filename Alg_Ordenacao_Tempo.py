#Lucas Domingos Leão Gomes

def selection(v):
    ordenado = []
    while v:
        ordenado.append(min(v))
        v.remove(min(v))
    return ordenado
    


from random import random, shuffle
lista = list(range(20))
shuffle(lista)
print(selection(lista))