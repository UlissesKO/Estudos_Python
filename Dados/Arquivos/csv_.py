import csv

#with open('Dados\Arquivos\csv.csv', 'w') as arq:

    #Cria o "escritor"
    #escrita = csv.writer(arq)

    #Escreve as linhas
    #escrita.writerow((43, 65, 12))

with open('Dados\Arquivos\csv.csv', 'r') as arq:
    data = arq.read()

    print(type(data))