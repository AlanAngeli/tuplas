tupla = 1,2,3,"a", "Alan"
tupla2 = 1,2,3,4,5
tupla3 = 6,7,8,9,"yy"
tupla4 = tupla + tupla2 + tupla3

print(tupla2 + tupla3)
print(tupla4)

n1, n2, n3, *_, n10 = tupla4

print(n10)