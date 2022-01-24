def filtrarNumerosLetras(entrada):
    numeros = ""
    letras = ""

    for caracter in entrada:
        if ord(caracter) in range(48, 58):
            numeros += caracter
        else:
            letras += caracter

    return (numeros, letras)

def solve(numeros, letras):
    primeraMitad = int(numeros[:(len(numeros)//2)])
    segundaMitad = int(numeros[len(numeros)//2:])
    sumaMitades = primeraMitad + segundaMitad
    
    cadenaOrdenada = "".join(sorted(letras))

    return (sumaMitades, cadenaOrdenada)

if __name__ == "__main__":
    entrada = input("Introduzca una palabra: ")
    numeros, letras = filtrarNumerosLetras(entrada)
    sumaMitades, cadenaOrdenada = solve(numeros, letras)
    print(f"suma de numeros = {sumaMitades}, cadena = {cadenaOrdenada}")
