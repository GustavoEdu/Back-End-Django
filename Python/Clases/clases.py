import time # o.O
from motor import Motor

class Carro: # Los paréntesis no son obligatorios
    # Variables de Clase
    idx = 0

    def __init__(self, motor, marca, modelo, color, cant_puertas, ltr_tanque): # mi_mismo, self es una convención
        # Variables de Instancia
        self.motor = motor
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cant_puertas = cant_puertas
        self.ltr_tanque = ltr_tanque

    # Comportamientos
    def encender_motor(self): # self es necesario para hacer uso de las Variables de Instancia
        print("Motor Encendido...")
        time.sleep(1)
    
    def acelerar(self):
        print("Acelerando...")
        time.sleep(2)

    def frenar(self):
        print("El coche está frenando...")
        time.sleep(3)
        print("El coche se detuvo")
        time.sleep(1)

    def __str__(self): # .toString() en Java
        return \
f"""
Marca: {self.marca}
Modelo: {self.modelo}
Color: {self.color}
Puertas: {self.cant_puertas}

Características del Motor:
{self.motor.__str__()}
""" # BLOCK en Perl

Carro.idx = 1

motor_1 = Motor("Diesel", 2.0)
motor_2 = Motor("Eléctrico", 3.0)

carro_1 = Carro(motor_1, "Subaru", "Impreza", "Negro", 4, 40)
carro_2 = Carro(motor_2, "Mazda", "BT-50", "Gris", 4, 45)

carro_1.encender_motor()
carro_1.acelerar()
carro_1.frenar()

carro_2.encender_motor()
carro_2.acelerar()
carro_2.frenar()

print(carro_1)
print()
print(carro_2)
