lista=[1,2,2,3,3,3,4,5,5,6,6,6,6]
for num in lista:
  if lista.count(num) >= 2:
    lista.remove(num)
    x=len(lista)
print lista
  
