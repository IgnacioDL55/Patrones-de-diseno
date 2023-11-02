from Tv import Tv

class Plasma(Tv):
    def __init__(self, marca="Noblex", pulgadas=32, color="Azul", precio=200, angulo_vision=85, tiempo_respuesta=5):
        super().__init__(marca, pulgadas, color, precio)
        self.angulo_vision = angulo_vision
        self.tiempo_respuesta = tiempo_respuesta
        self.descripcion = "Plasma... próximamente será un LED"

    def get_angulo_vision(self):
        return self.angulo_vision

    def get_tiempo_respuesta(self):
        return self.tiempo_respuesta
    
    def get_descripcion(self):
        return self.descripcion