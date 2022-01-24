def obtenerElementoMayorFrecuencia(lista):
    nombres_y_frecuencias = {}
    for nombre in lista:
        if(not nombre in nombres_y_frecuencias.keys()):
            nombres_y_frecuencias[nombre] = 1
        else:
            nombres_y_frecuencias[nombre] += 1
    aux = sorted(nombres_y_frecuencias, key = nombres_y_frecuencias.get)
    elementoMayorFrecuencia = aux[len(aux) - 1]
    mayorFrecuencia = nombres_y_frecuencias[aux[len(aux) - 1]]
    return (elementoMayorFrecuencia, mayorFrecuencia)

if __name__ == "__main__":
    lista_nombres = ["Ana", "Jhon", "Daniel", "Melissa", "Juan", "Melissa", "Daniel", "Ana", "Melissa"]
    elemento, frecuencia = obtenerElementoMayorFrecuencia(lista_nombres)
    print(f"Elemento: {elemento}")
    print(f"Frecuencia: {frecuencia}")

    numeros = [4, 5, 2, 9, 0, 34, 5, 7, 9, 54, 0, 5, 9, 7, 4, 2, 0, 0]
    elemento, frecuencia = obtenerElementoMayorFrecuencia(numeros)
    print(f"Elemento: {elemento}")
    print(f"Frecuencia: {frecuencia}")
