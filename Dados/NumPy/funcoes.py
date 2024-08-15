import numpy

#Arrays
array1 = numpy.array([10, 31, 54, 25, 43, 34, 45, 54, 90, 23])
print(array1)
print(type(array1))
print(array1.shape)
print("_____________", "Indexação")

index = [0, 2, 4, 6]
print(array1[index]) #Pode usar uma lista no lugar do index
print("\nMascára")

mask = (array1 % 2 == 0) #Vai dividir todos os elementos do array por 2 e retornar um boolean, nesse caso True para os pares
print(mask)

print(array1[mask])
print("_____________", "\nFunções")
array2 = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array2)
#Soma acumulada dos elementos
print(array2.cumsum())
#Multiplicação acumulada dos elementos
print(array2.cumprod())

array3 = numpy.arange(0, 50, 3) #Cria um array que começa do 0 e vai até o 50, mas pulando de 3 em 3. Por isso pede 3 argumentos
print("\n", array3)

array4 = numpy.zeros(10) #Cria uma matriz só de zeros, é util para criar um inicio para um modelo de ia por exemplo., Ex.: numpy.zeros(5, 2, 3)
print("\n", array4)

array5 = numpy.ones(5)#Cria uma matriz só de um. Se colocar mais parametros ele cria uma matriz. Ex.: numpy.ones(5, 2, 3) 1º parametro - Linhas
print("\n", array5)                                                                                                      #2º parametro - colunas
                                                                                                                         #etc.
array6 = numpy.eye(5) #Cria uma matriz diagonal com neste caso 5 linhas, serve pra várias expressões matematicas. É de 2 dimensões
print("\n", array6)
print(array6.shape)

array7 = numpy.diag(array1) #Cria uma matriz diagonal também, mas com os valores do array1 
print("\n", array7)

print("Media\n", numpy.mean(array3)) #É a média do array

print("Desvio Padrão\n", numpy.std(array3)) #É o desvio padrão do array, fala se os dados estão muito afastados da media

print("Variância\n", numpy.var(array3)) #É a variancia do array, fala se os dados estão muito afastados da media

print("Soma\n", numpy.sum(array3)) #É a soma dos elementos do array

print("Multiplicação\n", numpy.prod(array3)) #É a multiplicação dos elementos do array

print("Soma cumulativa\n", numpy.cumsum(array3)) #É a vsoma cumulativa dos elementos do array. tem o cumprod() tambem

print("Juntar arrays\n", numpy.add(array2, array1)) #Soma cada elemento de um array com o elemento correspondente dos arrays seguintes
                                                                #Só funciona com 2 arrays

print("Multiplicar matrizes\n")
matriz1 = numpy.array([[2, 4, 10], [6, 8, 12]])#Número de colunas da primeira matriz
matriz2 = numpy.array([[1, 3], [5, 7], [9, 11]])#Igual ao numero de linhas da segunda matriz

print(matriz1 @ matriz2) #@ é o operador de multiplicação de matrizes

print("\n", array1, array1 * 15)