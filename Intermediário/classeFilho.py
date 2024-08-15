class classePai:
    def __init__(self, fale):#isso é um metodo dunder
        self.fale = fale
    def sayThis(self):
        print(self.fale)

obj = classePai("boi tata")
obj.sayThis()

class classeFilho(classePai):
    def __init__(self, fale): #ao criar um init aq, vc deleta todos os parametros q veio da funçao pai
        super().__init__(fale)#super() serve pra pegar os parametros de volta
        self.fale2 = "teste muit bacanal"
    def sayThis(self):
        print(self.fale, self.fale2)

obj2 = classeFilho("fdsafdas")
obj2.sayThis()


print(dir(classePai))#Mostra os metodos Dunder de cada classe, pode ser de tipo de dados tbm