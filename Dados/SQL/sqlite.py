import sqlite3
import pandas

#Esta criando um objeto para conectar ao banco de dados
db = sqlite3.connect('Python\Dados\SQL\DataBase.db')

#É o que percorre os dados dentro do banco de dados
cursor = db.cursor()

#Usa aspas duplas tres vezes pois tem aspas simples dentro da função
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table'"""
                #^^^^ É SQL
#SELECT - vai buscar um campo, neste caso chamado name
#FROM - vai falar de onde vai buscar o campo
#WHERE - só vai retornar o que satisfazer a condição, no caso é uma tabela

#Vai executar o query escrita acima
cursor.execute(sql_query)#Execute é um metodo do objeto cursor

#Vai mostrar o resultado da consulta
print(cursor.fetchall(), "\n")#Fetchall é o metodo do cursor para mostrar a consulta
#Aqui mostra os nomes de todas as tabelas

#O * retorna todo o conteudo do FROM
sql_query = 'SELECT * FROM tb_vendas_dsa'  
cursor.execute(sql_query)

#Aqui é list comprehensions, é criar um loop para criar uma nova lista em cima de uma já existente
nomes_colunas = [description[0] for description in cursor.description]
#description é um atributo de um objeto, neste caso tem o nome de todas as colunas

print(nomes_colunas, "\n")

cursor.fetchall()

#Calcular a média de alguma coluna
sql_query = 'SELECT AVG(Unidades_vendidas) FROM tb_vendas_dsa'
#AVG() - vai fazer a média dos dados do metadado especificado nos parenteses

cursor.execute(sql_query)

print(cursor.fetchall(), "\n")

#Calcular média vendida de determinado produto
sql_query = 'SELECT Nome_Produto, AVG(Unidades_vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto'
            #A coluna que não esta na função vai para o group by

cursor.execute(sql_query)
print(cursor.fetchall(), "\n")

#Vai mostrar a média de unidades vendidas somente para intens com valor unitarios menor que 199
sql_query = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
               FROM tb_vendas_dsa
               WHERE Valor_Unitario > 199
               GROUP BY Nome_Produto"""

cursor.execute(sql_query)
print(cursor.fetchall(), "\n")

