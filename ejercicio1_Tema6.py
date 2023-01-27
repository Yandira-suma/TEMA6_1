class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


def caracteristica(lista):
    for vehiculo in lista:
        print(type(vehiculo).__name__, vehiculo.__dict__)


d = Coche("negro", 4, 5, 250, 400)
lista_vehiculos = [ d ]
caracteristica(lista_vehiculos)