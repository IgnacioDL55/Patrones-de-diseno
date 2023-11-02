class Tv:
    def __init__(self, marca, pulgadas, color, precio):
        self.marca = marca
        self.pulgadas = pulgadas
        self.color = color
        self.precio = precio

    def clone(self):
        import copy
        return copy.copy(self)