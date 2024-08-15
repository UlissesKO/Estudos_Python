import pandas

file = "Python\Dados\Arquivos\salary.csv"

#Vai abrir o arquivo
data = pandas.read_csv(file)

#Mostra as primeiras linhas
print(data.head(10), "\n")


#Conta os valores da coluna especificada
print(data['Job Titles'].value_counts(), "\n")

#o isna() verifica quando tem celulas sem nenhum dado
print(data.isna(),"\n")
                #O sum() vai contar todas as celulas sem dado de cada coluna
print(data.isna().sum(),"\n")

print("Quantidade de Rows: ", len(data.index), "\n")

#Corrigindo os dados faltando
                        #Contar os valores da coluna
modaHoras = data['Typical Hours'].value_counts().index[0]
                                           #Pegar o que mais apareceu
print(modaHoras, "\n")

                        #Contar os valores da coluna
modaSalario = data['Annual Salary'].value_counts().index[0]
                                           #Pegar o que mais apareceu
print(modaSalario, "\n")

#Vai preencher os na da coluna especificada
                                      #Salva as modificações no dataframe
data.fillna({'Typical Hours' : modaHoras}, inplace=True)

data.fillna({'Annual Salary' : modaSalario}, inplace=True)

data['Hourly Rate'] = ((data['Annual Salary'] / 12) / 4) / data['Typical Hours']

#Esta separando o sobrenome do primeiro nome
data['Surname'] = data['Name'].str.split(', ').str[0]
                            #str - diz que esta separando uma string
                            #split - é o metodo de divisao
                            #.str[0] - esta pegando o primeiro valor da lista que é retornada

data['First Name'] = data['Name'].str.split(', ').str[1]

#Ta excluindo a coluna 'Name' pq to separando o conteudo dela em duas colunas
data.drop(columns=['Name'], inplace=True)

#Ta inserindo as colunas no index especificado
data.insert(0, 'First Name', data.pop('First Name'))
data.insert(1, 'Surname', data.pop('Surname'))


print(data.head(10), '\n')
print(data.isna().sum(),"\n", data.dtypes, "\n")

#Resumo estatisco da coluna Annual Salary
print(data['Annual Salary'].describe(), "\n")

#Vai criar um novo dataFrame com só os salarios acima da média
data2 = data.query('`Annual Salary` > 114264.000000')

print("Sálarios acima de média\n\n", data2.describe(), "\n", data2.head(15), "\n")
print(data2['Job Titles'].value_counts(), "\n")
print("Quantidade de Rows: ", data2.shape, "\n")

#Procura determinados valores dentro da coluna especificada
print(data['Job Titles'].isin(['SERGEANT']), "\n")
                #groupby vai agrupar as colunas em grupos, neste caso agrupar todos os job titles dentro de um só department
data3 = data[['Department', 'Job Titles', 'Annual Salary', 'Hourly Rate']].groupby(['Department', 'Job Titles']).mean()
#Criou uma nova tabela neste formato                                #.mean() mostra a media da coluna não especificada nesta parte
print(data3, "\n\n\n")

#Cria um novo dataframe baseado no groupby do arquivo csv completo                                                                                                
data3 = data[['Department', 'Job Titles', 'Annual Salary', 'Hourly Rate']].groupby(['Department', #.agg vai adicionar vários metodos matematicos
                                                                                     'Job Titles']).agg(['mean', 'median', 'count', 'max', 'min'])
                                                                                     #O de cima só vai mostrar a média
print(data3,'\n') 

#Cria um grafico deste dataframe
import matplotlib.pyplot as plt
#Cria o grafico
data.plot()

#Gráfico de dispersão
data.plot.scatter(y= 'Annual Salary', x='Typical Hours')

#Mostra o gráfico
plt.show()


#TEM MUITO MAIS COISA DO PANDAS