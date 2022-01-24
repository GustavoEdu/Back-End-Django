#%%
print("Hola Mundo")

# Comentarios de una línea
"""
****** Inmutables ******
str: "Cadenas de Texto"
float: 3.141592e1
int: 23
boolean: True o False
tuple: (1, 2, 3) o (1,) - No se puede Editar

****** Mutables ******
No hacemos cambios en su Referencia
list (Arreglos): [1, 2, "String", True, 1.0, (1, 2, 3)] - Es muy parecido a JavaScript
set (Listas desordenadas): {int, str, bool, tuple, bool} - No consdiera el segundo bool 
dict: {'key': 'value', , ,} - Es recomendable que la llave sea inmutable
"""
#- Operadores aritméticos
#- '+'
#- '-'
#- '/' - División Flotante - Nos da una Cantidad Limitada de Decimales
#- '//' - División Entera - 2.999999 => 2
#- '**' 2 ** 4 == 2 * 2 * 2 * 2
#- '%', 4 % 2 == 0
#- abs(-100), 100
#-

print(abs(-100))
a = 3.1 + 3.2
b = 4.3 + 3.2
print(a == 6.3) # Configuración de nuestra Computadora
print(a)
print(b == 7.5)
print(b)

# a = 13 / 14
# print(a) # El Hardware de la Computadora se Encarga
# print#(f'{a:.1}')

# Métodos de comparación

#- < menor que
#- <= menor igual que
#- > mayor que
#- >= mayor igual que
#- == comparación (= asignación)
#- != distinto

print(3 > 3) # False
print(3 >= 3) # True
print(2 == 2) # True
print('hola' == 'Hola') # False, Python es Case-Sensitive, compara según ASCII
print(str == str) # False
print('hola' != 'Hola') # True

#- Valores booleanos - Con mayúsculas
a = True # 1 - Truthy
b = False # 0 - Falsy
print(2 + a + b)

# Operadores Lógicos
#- or (a or b) ya no || (a || b)
#- and (a and b) ya no && (a && b)
#- not (not a) ya no ! (!a)
print((True or False) and False) # Se evalúa de Izquiera a Derecha and >>> or
print(True and False)
print(not True)

#- Operadores de asignación

#- =
#- +=
#- -=
#- *=
#- /=
#- //=
#- **-
a = 3
print(a)
a += 1
print(a)
a -= 1
print(a)

cadena = "Cadena" # Detecta que no está en uso y pasa al Garbage Collector
print(id(cadena)) # 222
cadena += "de carácteres"
print(cadena)
print(id(cadena)) # 666

# Operadores de Pertenencia - Evitar los Truthy y Falsy
#- in (=== en JavaScript)
#- not in (!== en JavaScript)

a = [1, 2, "3"]
print("3" in a)
print(3 in a)

b = {'1': "uno", 2: "dos"}
print(1 in b) # Solo itera por las llaves
print("uno" in b.values())

# Operadores de identidad
#- is
#- is not
a = 1
b = True # b = a - Ahorra Espacio
print(a is b)  # Son el mismo objeto, tienen las mismas referencias
print(a is not b)  # No son el mismo objeto, no tienen las mismas referencias
print(a == b)
print(id(a))
print(id(b))

# Declaración de Variables
# Las Variables nunca comienzan con Mayúsculas, las Clases sí
Variable = 1 # no
variableNumero = 2

variable_numero = 3 # Recomendado por la Documentación
# 2variable # No
variable_2 = 5
# Tipos Especiales
_variable = 6
__variable = 666
VARIABLE = "Valor Constante" # Constante
# VARIABLE = 2 # No

# Destructuring
x, y, z = (1, "Django", True) # Esto es una Tupla por las Comas

arr = [34, 1.0, 1.5]
print(sum(arr)) # Hay que conocer los Nombres Reservados para evitar la Sobreescritura de Funciones

# Mañana veremos la Entrada y Salida Estándar y Funciones Propias de los Tipos de Datos
# Ejercicios Básicos

"""
str,
int,
list,
dict
"""
#%%
# Conversión de Tipos de Datos
a = "Gustavo"
nombres = "Gustavo"

cadena_numerica = "1234567"
cadena_numerica_2 = "1234567"
print(cadena_numerica + cadena_numerica_2)

# Casteamos
numeros = int(cadena_numerica)
numeros_2 = int(cadena_numerica_2)

numero_pi = "3.141519"
numero_a_float = float(numero_pi)
print(numeros + numeros_2 + numero_a_float)
#%%

#%%
# Condicionales
# if else elif

# Apuntan al mismo Espacio de Memoria
a = 0
b = 1

if a > b:
    print("a es ganó a b")
else:
    print("b ganó a 'a'")

# Tener Cuidado con la Indentación, Tab o 4 Espacios

if a != b:
    pass # Para dejar en Blanco
elif b is a:
    print("a y b se guardan en el mismo espacio")    
else:
    print("b ganó a 'a'")

if not a: # Truthy
    print("entro al not")

#%%
#%%
# Ingreso de Datos
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
print(f"Tu nombre es {nombre} {apellido}")
#%%

#%%
a = None # Proximamente será utilizada
a = 1
