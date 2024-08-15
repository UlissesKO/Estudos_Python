#Expressões regulares
import re

texto = "ghajsfgjoi woijsedafihabewsiv bjnfv lknmv aj bfibdhfbwu9erhth@#$#%RJNBKhufdsa bh3$R#OJ"
        #findall procura tal coisa na string
print(re.findall("a", texto))
print("a apareceu ",len(re.findall("a", texto)), " Vezes")

print("-")
                      #Código de filtragem
print(re.findall(r"aj (\w+)", texto))
                #r deixa o python reconhecer a \ como código