def normalizar(num):
    return round(num * 100000) / 100000

def sumar(num1, num2):
    return normalizar(num1 + num2)

def restar(num1, num2):
    return normalizar(num1 - num2)

def multiplicar(num1, num2):
    return normalizar(num1 * num2)

def dividir(num1, num2):
    if(num2 == 0):
        raise Exception()
    return normalizar(num1 / num2)

def modulo(num1, num2):
    return num1 % num2
