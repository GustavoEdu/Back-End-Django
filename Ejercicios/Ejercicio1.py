def buscarElemento(elemento, lista):
    return lista.index(elemento) if (elemento in lista) else None

if __name__ == "__main__":
    lista = [3, "Hello World", 4, "jijijija", [1, 2, 3, 4], (666, 404, 200)]
    print(buscarElemento((666, 404, 200), lista))
