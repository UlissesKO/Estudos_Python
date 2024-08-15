import pandas
import matplotlib.pyplot as plt
import seaborn
import numpy
import datetime

df = pandas.read_csv('Python\Dados\Projeto 2\dataset.csv')


#Pergunta 1
#Filtra o dataframe original para pegar somente a categoria office suplies
valorVenda = df[df['Categoria'] == 'Office Supplies']

#Filtra o dataframe ja filtrado pra criar outro somente com o valor de venda maximo
valorVenda = valorVenda[valorVenda['Valor_Venda'] == valorVenda['Valor_Venda'].max()]

print("Pergunta 1:\n", valorVenda['Cidade'], "\n")


#Pergunta 2
data = df[['Data_Pedido', 'ID_Pedido']].groupby(['Data_Pedido']).size().reset_index(name='Contagem')
#Gráfico

seaborn.barplot(x=data['Data_Pedido'], y=data['Contagem'])
plt.title('Pergunta 2')
plt.show()


#Pergunta 3
data = df[['Estado', 'ID_Pedido']].groupby(['Estado']).size().reset_index(name='Contagem')

seaborn.barplot(x=data['Estado'], y=data['Contagem'])
plt.title('Pergunta 3')
plt.show()


#Pergunta 4
data = df[['Estado', 'ID_Pedido']].groupby(['Estado']).size().reset_index(name='Contagem')
data = data.sort_values(by='Contagem', ascending=False).reset_index()

seaborn.barplot(x=data['Estado'].head(10), y=data['Contagem'])
plt.title('Pergunta 4')
plt.show()


#Pergunta 5
data = df[['Segmento', 'ID_Pedido']].groupby(['Segmento']).size().reset_index(name='Contagem')
data = data.sort_values(by='Contagem', ascending=False).reset_index()

plt.pie(data['Contagem'], labels=data['Segmento'])
plt.title('Pergunta 5')
plt.show()

