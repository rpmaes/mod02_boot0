from functools import reduce

lista = [1, 3, -1, 15, 9]

sumatorio = reduce(lambda x, y: x + y, lista)

#Creo una copia de  la lista
l = lista[:]

# añado el neutro para la suma en la posicion cero
l.insert(0,0)

sumatorioDobles = reduce(lambda x, y : x + y*2, lista)


print(sumatorio)
print(sumatorioDobles)
