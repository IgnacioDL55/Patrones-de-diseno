class Auto:
    def __init__(self):
        self.cantidad_de_puertas = 0
        self.modelo = ""
        self.marca = ""
        self.motor = None

    def get_cantidad_de_puertas(self):
        return self.cantidad_de_puertas

    def set_cantidad_de_puertas(self, cantidad_de_puertas):
        self.cantidad_de_puertas = cantidad_de_puertas

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_motor(self):
        return self.motor

    def set_motor(self, motor):
        self.motor = motor
