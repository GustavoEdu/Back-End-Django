from calculadora import sumar, restar, multiplicar, dividir, modulo 

if __name__ == "__main__":
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Módulo")

    op = input("Selecciona una Operación: ")
    num1, num2 = None, None
    if(int(op) in range(1, 6)):
        num1 = float(input("Operador A: "))
        num2 = float(input("Operador B: "))

    resultado = None
    if op == "1":
        resultado = sumar(num1, num2)
    elif op == "2":
        resultado = restar(num1, num2)
    elif op == "3":
        resultado = multiplicar(num1, num2)
    elif op == "4":
        try:
            resultado = dividir(num1, num2)
        except Exception:
            print("¡No es posible dividir entre 0!")            
            exit()
    elif op == "5":
        resultado = modulo(num1, num2)
    else:
        resultado = "¡Entrada no válida!"
    
    print(f"El resultado es: {resultado}")
