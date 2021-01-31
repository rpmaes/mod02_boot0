def sumatorio(n):
    if n != 0:
        return n + sumatorio(n-1)
    else:
        return 0

sumatorio (4)

#hacer yo el factorial recursivo
def factorial(n):
    if n != 1:
        return n * factorial(n-1)
    else:
        return 1
