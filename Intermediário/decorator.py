import requests

#criando o decorator
def decorator(funcao):
    def wrapper(): # vai executar oq vai mudar na funçao e a funçao
        print("antes")#coisa q vai fazer antes da funçao
        funcao() #vai executar a funçao a ser mudada
        print("depois")#executa depois da funçao
        

    return wrapper #vai voltar a wrapper




#pegar o preço do dolar
@decorator
def preço_dolar():
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisiçao = requests.get(link)
    requisiçao = requisiçao.json()
    a = "antes bem antes"
    print(a)
    print(requisiçao['USDBRL']['bid'])

preço_dolar()