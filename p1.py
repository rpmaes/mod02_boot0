def sumaTodos(limitTo):
    resultado = 0
    for i in range (0, limitTo+1):
        resultado += i
        
    return resultado

def sumaTodosLosCuadrados(limitTo):
    resultado = 0
    for i in range(limitTo):
        resultado += i *i
    return resultado

print(sumaTodos(4))
print(sumaTodosLosCuadrados(3))