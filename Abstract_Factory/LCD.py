from Tv import Tv

class LCD(Tv):
    def __init__(self, marca="Samsung", pulgadas=32, color="Amarillo", precio=250, costo_fabricacion=140):
        super().__init__(marca, pulgadas, color, precio)
        self.costo_fabricacion = costo_fabricacion
        self.descripcion = "LCD"

    def get_costo_fabricacion(self):
        return self.costo_fabricacion

    def set_costo_fabricacion(self, costo_fabricacion):
        self.costo_fabricacion = costo_fabricacion

    def get_descripcion(self):
        return self.descripcion