#%% Strings "" ''

a = "Hola mundo"

# indices 0, 1, 2, ...
print(a[0])

#%% Slice
a = "Hola mundo"
b = a[:]
print(b)
b = a[4:7]
print(b)
b = a[::-1] # Invierte una Palabra
print(b)

#%% 
cadena = "Hola mun d o"
ca = cadena.split(" ")
print(ca)
ca = "-".join(ca)
print(ca)

#%% Imprimir por Pantalla
a = "Gustavo"
b = 23
# s: String
# d: Dígito
print("%s %d" % (a, b))
print("{} {}".format(a, b))
print(f"{a} {b}")

# No utilices ñ
# %%
"""
equipos_tecnologicos = "portatil,celular,usb,reloj,inteligente"
"""
#%% Ejercicio
equipos_tecnologicos = "portatil,celular,usb,reloj,inteligente"
equipos_tecnologicos = equipos_tecnologicos.split(",")
for i in range (0, len(equipos_tecnologicos)):
    print(f"Equipo Tecnológico #{i + 1}: {equipos_tecnologicos[i]}")

# %%
