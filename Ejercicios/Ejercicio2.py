def obtenerMaximoEspecial(lista):
    return max(list(map(abs, lista)))

if __name__ == "__main__":
    lista = [5, 3, 8, -9, 12, -34, 35, -40]
    print(obtenerMaximoEspecial(lista))
