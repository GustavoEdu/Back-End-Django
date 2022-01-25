# Herencia
class Animal: # object es como Object de Java
    def __init__(self, edad, max_energia, min_energia):
        self.edad = edad
        self._max_energia = max_energia # _ indica que es un método protegido
        self._min_energia = min_energia # __ indica que es un método privado
    
    def cazar(self):
        pass
            
    def alimentarse(self):
        pass

    def tiene_hambre(self):
        return self.energia <= self._min_energia

class Gato(Animal):
    def __init__(self, nombre, edad, max_energia, min_energia):
        super().__init__(edad, max_energia, min_energia)
        self.energia = self._max_energia
        self.nombre = nombre

    def cazar(self):
        self.energia -= 2        
        print(f"{self.nombre} está cazando")
        comer = self.tiene_hambre()
        if comer:
            print("Comiendo lo que cazó")
    
    def dormir(self):
        print("El gato está durmiendo")

gato_1 = Gato("Michi", 5, 6, 2)
gato_1.cazar()   
print(gato_1.tiene_hambre())
gato_1.cazar()   
print(gato_1.tiene_hambre())
gato_1.cazar()   
print(gato_1.tiene_hambre())
gato_1.dormir()
