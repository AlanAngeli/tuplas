t1 = (1,2, "Alan", 4,5) * 5

print(t1)
print()

t2 = 1,2,3,4,5
t2 = list(t2) #convertendo a tupla em lista
t2[2] = 100
print(t2)
print()
t2 = tuple(t2) #convertendo a lista em tupla