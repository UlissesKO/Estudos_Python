#JSON é organizado em forma de dict
import json 

dict = {"Marca":"Chevrolet",
        "Modelo":"Opala Coupe",
        "Motor":"6 Caneco",
        "Ano":"1981"}

#Converte o dict para json
json.dumps(dict)

#Cria o arquivo json
with open("Dados\Arquivos\json_.json", "w") as arq:
    arq.write(json.dumps(dict))

with open("Dados\Arquivos\json_.json", "r") as arq:
    text = arq.read()
    data = json.loads(text)

for i, k in data.items():
    print(i, k)