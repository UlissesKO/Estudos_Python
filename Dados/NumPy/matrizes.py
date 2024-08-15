import numpy
import os


#2 dimensões
matriz1 = numpy.array([ [1, 2, 3], [4, 5, 6] ])
print(type(matriz1), "\n", matriz1.shape, "\n", matriz1)

print("_____________")

#3 dimensões
matriz2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = numpy.matrix(matriz2)
print(type(matriz2), "\n", matriz2, "\n", matriz2.shape)

print("_____________", "\nIndexação")

#O primeiro numero é a linha e o segundo é a coluna
print(matriz2[1, 2])

#Manipulando arquivos
print("----------------------\nAbrindo arquivos com o numpy")
filename = os.path.join('Python\\Dados\\NumPy\\csv.csv')

array1 = numpy.loadtxt(filename, delimiter=",", usecols=(0, 1, 2), skiprows=1)
#filename = nome do arquivo,    delimiter = o que vai separar as colunas
#usecols = Vai selecionar quais colunas vai importar pra array (opcional dependendo do dataset)
#skiprows = Vai escolher quantas linhas vai pular (opcional dependendo do dataset)

for i in array1:
    print(i)
