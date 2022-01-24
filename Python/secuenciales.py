#%% Tuplas
# Nos ayudan a agrupar datos relacionados
import abc


numeros = 1, 2, 3
tupla_tipo_datos = str, int, list, tuple
# Es recomendable no mezclar los tipos de datos

tupla = ()
tupla = tuple() # Constructor

print(tupla_tipo_datos[0])
print(tupla_tipo_datos[1])
print(tupla_tipo_datos[2])
print(tupla_tipo_datos[3])

compra = "usb", 3, 3.99
print(f"Artículo comprado: {compra[0]}\nCantidad: {compra[1]}\nPrecio: {round(compra[1] * compra[2])}")
# %%

#%% Desempaquetar una Tupla
compra = "usb", 3, 3.99
objeto, cantidad, precio = compra
print(f"Artículo comprado: {objeto}")
print(f"Cantidad: {cantidad}")
print(f"Precio: {cantidad * precio}")

# %%
numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10
print(numeros[:5])
print(numeros.count(10))
print(numeros.index(6)) # Tener asegurado de que se pueda conseguir dicho valor
print(len(numeros))

#%% Listas
# Normalmente, solemos agrupar datos del mismo tipo
lista = []
lista = list()
lista = [bool, str, int, float, ...]

nombres = ["Jhon", "Ana", ...]
matriz = [[1, 2], [4, 3]]
print(matriz[0][1])

# %% Crear lista con split()
computador = "monitor,torre,teclado"
armar_pc = computador.split(",")
print(armar_pc)

armar_pc.append("raton") # Agregamos un elemento
print(armar_pc)

utileria = ["camara", "bafles"]
armar_pc += utileria # Es posible juntar listas
print(armar_pc)

# indexamos
print(armar_pc[0])
print(armar_pc[1])
print(armar_pc[2])
print(armar_pc[-3])
print(armar_pc[:-1])

armar_pc[0] = "televisor" # Hacer un cambio en una posición de lista
print(armar_pc)

# Agregar en una posición
armar_pc.insert(0, "mesa")
print(armar_pc)

# Preguntar si hay un elemento
print("mesa" in armar_pc)
print("mesa escritorio" in armar_pc)

# Replicar
print(armar_pc * 2)

# Borrado de Elementos
if "mesa" in armar_pc:
    armar_pc.remove("mesa")

print(armar_pc)

#%% ordenar elementos sort()
abecedario = ["s", "d", "r", "a", "f"]
abecedario.sort()
print(abecedario)
abecedario.sort(reverse = True)
print(abecedario)
# %%
abecedario = ["s", "d", "r", "a", "f"]
letras_ordenadas = sorted(abecedario)
print(letras_ordenadas)
print(abecedario)
# %%
""" Funciones útiles
sorted(abcdario) # ordenar
abcdario.count("a")
min(numeros)
max(abcdario)
abs(-1)
"""

#%% Borrar elementos
abcdario = ["s", "d", "r", "a", "f"]
abcdario.remove("s")
print(abcdario)

# pop()
ele = abcdario.pop(1)
print(ele)
print(abcdario)

# Es usualmente el for in el indicado
for i in abcdario:
    print(i)
#%% Diccionarios, semejante a JSON
di = {}
di = dict()

persona = {
    "nombre": "Gustavo",
    "ciudad": "Tacna",
    "len-pro": ["Java", "JavaScript", "Python", "Perl"]
}
print(persona["nombre"])

persona["apellido"] = "Jeager" # Se agrega al último
print(persona)

del persona["apellido"] # Se podría utilizar también pop, solo que pasaremos la llave, aunque es limitado
print(persona)

# popitem
c = persona.popitem()
print(c)
print(persona)

# clear()
persona.clear()
print(persona)
# %%
