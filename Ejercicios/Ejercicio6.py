if __name__ == "__main__":
    personas = []
    while True:
        print("1.- Agregar Persona")
        print("2.- Consultar Personas")
        print("3.- Salir")
        
        op = input("Introduzca una opción: ")
        
        if op == "1":
            nombre, apellido, ciudad = input("Nombre: "), input("Apellido: "), input("Ciudad: ")
            lenguajes_programacion = []
            
            conoce = input("¿Conoce algún Lenguaje de Programación? (y/n): ")
            if conoce == "y":
                while True:
                    lp = input("Introduzca un Lenguaje de Programación: ")
                    lenguajes_programacion.append(lp)

                    continuar = input("¿Desea agregar otro Lenguaje de Programación? (y/n): ")
                    if continuar == "n":
                        break
            
            persona = {
                "nombre": nombre,
                "apellido": apellido,
                "ciudad": ciudad,
                "lenguajes_programacion": lenguajes_programacion
            }
            personas.append(persona)

        elif op == "2":
            for i in range(len(personas)):
                print(f"Persona #{i + 1}:")
                print(f"Nombre: {personas[i]['nombre']}")
                print(f"Apellido: {personas[i]['apellido']}")
                print(f"Ciudad: {personas[i]['ciudad']}")

                print("Lenguajes de Programación:")
                for j in range(len(personas[i]['lenguajes_programacion'])):
                    print(f"Lenguaje #{j + 1}: {personas[i]['lenguajes_programacion'][j]}")
                print()
        elif op == "3":
            exit()
        else:
            print("Entrada no válida")
