a = {"edfa", "Fsadd", "dasd"}#Sets
print(type(a))
print(a)

b = set()#Sets
b.add(1)
b.add(2)
b.add(3)
b.add(4)
print(type(b))
print(b)

c = {"Magnussen": "Haas", "Carlos Sainz":["Toro rosso", "Ferrari"]} #dictionary
print(c["Magnussen"])
c["Verstappen"] = "Red Bull"

for i in c:
    print(i)
    print(c[i])