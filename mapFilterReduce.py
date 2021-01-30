from functools import reduce

def dobles(x):
    return x+x


lista = [1, 3, -1, 15, 9]

listaDobles = map(lambda x: x*2, lista)
listaDobles = map(dobles,lista)


def esPar(x):
    return x % 2 == 0
        
listaPares = filter(lambda x: x % 2 == 0, lista)
listaPares = filter(esPar, lista)

sumatorio = reduce(lambda x, y: x + y, lista)

suma100 = reduce(lambda x, y: x + y, range (101))

sumatorioDobles = reduce(lambda x, y : x + y*2, lista)
