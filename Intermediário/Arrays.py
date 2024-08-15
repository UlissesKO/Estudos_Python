import array as arr

q = "\n"

a = arr.array("i", [1, 2, 3, 4, 6, 3, 8, 12, 1])

print(a)#forma mais rústica
print(q)

for i in a:#printa valor por valor da array
    print(i, end=" ")#end serve pra nao quebrar a linha pro proximo print
print(q)

a.insert(0, 2)

for i in a:
    print(i, end=" ")
print(q)

print(a[1])
print(q)

a.remove(2)
for i in a:
    print(i, end=" ")
print(q)

s_a = a[:5]
print(s_a)

a.extend([2, 5, 3, 5, 6])
for i in a:
    print(i, end=" ")
