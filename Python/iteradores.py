#%% Blucle for: Cuando conocemos la Cantidad de Iteraciones
for num in range(5): # 5 es no inclusivo (0, 5, 1) por default
    print(num)

for num in range(0, 10, 3): # 10 es no inclusivo
    print(num)

# %%
arrays = list(range(5))
print(arrays)

#%% break
numero = 5
for i in range(8):
    if i == numero:
        print("Encontré el número")
        break
    print("Buscando el  número")

# %% continue
for i in range(8):
    if i == 6 or i == 7:
        print("Estoy de Descanso")
        continue
    print("Estoy trabajando...")

# %% while: Cuando no conocemos la Cantidad de Iteraciones
"""
while condicion:
    hacer algo
"""
i = 0
while i < 10:
    print(1)
    i += 1


# %%
i = 0
while i < 8:
    print(i)
    if i == 4:
        print("Vamos por la mitad")
    i += 1

# %%
