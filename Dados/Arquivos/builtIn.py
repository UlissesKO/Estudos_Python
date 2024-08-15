#map
def potencia(x):
    return x ** 2

lista = [1, 2, 3, 4, 5, 6, 7]
           #Nome da função  #lista desejada
lista2 = list(map(potencia, lista))

print(lista2)

#reduce
from functools import reduce
#Não nescessariamente é soma, pode ser o maior, menor, etc
def soma(x, y):
    z = x + y
    return z

lista = [5, 3, 12, 54, 1, 43]
   #Nome da função  #lista desejada
print(reduce(soma, lista)) 

#Filter
def par(x):
    if x % 2 == 0:
        return True
    else:
        return False

print(list(filter(par, lista))) 

#zip
print(list(zip(lista, lista2)))