#%%
def convertir_tiempo(num):
    if len(str(num)) >= 2:
        hora = str(num // 60)
        minuto = num % 60
        str_minuto = str(minuto)
        return "{}: {}".format(hora, minuto)

print(convertir_tiempo(12345))
print(convertir_tiempo(7945))
print(convertir_tiempo(234))
print(convertir_tiempo(456))
print(convertir_tiempo(5678))

# %%
personas = ""
# CRUD => Create, Read, Update, Delete

def listar_nombres():
    global personas
    print(personas)

def crear_nombre(nombre):
    # Los nombres de las variables no deberías repetirse
    global personas # No es recomendable utilizar la palabra reservada global
    if len(personas) == 0:
        personas += nombre
    else:
        personas += "," + nombre

    # Todas las Funciones deberías retornar algo    
    return listar_nombres()

def crear_nombre_2(*nombre, **nombres):
    global personas # No es recomendable utilizar la palabra reservada global

    personas += ",".join(nombre)

    print(nombre)
    print(nombres)

    print("Añadido")
    return listar_nombres()
# %%
def actualizar_nombre(nom_actualizar, nom_nuevo):
    global personas
    if nom_actualizar in personas:
        personas = personas.replace(nom_actualizar, nom_nuevo)
        return listar_nombres()
    else:
        print("No se encuentra este nombre")

def eliminar_nombre(nombre):
    global personas
    lista_personas = personas.split(",")
    
    if nombre not in lista_personas:
        print("El nombre no se encuentra")
        return None # El return es un tipo de break para las Funciones
    
    else:
        lista_personas.remove(nombre)
        personas = ",".join(lista_personas) # Unir Listas o Tuplas
        return listar_nombres()

contexto = {
    "key": "valor",
    "er": "123"
}
crear_nombre_2("Juan", "Daniel", "Ronald", **contexto)

actualizar_nombre("Ronald", "Benito")

eliminar_nombre("Daniel")
# %%

# %%
