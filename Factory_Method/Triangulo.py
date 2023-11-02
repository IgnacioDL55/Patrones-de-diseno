from abc import ABC, abstractmethod

class Triangulo(ABC):
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    @property
    def ladoA(self):
        return self._ladoA

    @ladoA.setter
    def ladoA(self, ladoA):
        self._ladoA = ladoA

    @property
    def ladoB(self):
        return self._ladoB

    @ladoB.setter
    def ladoB(self, ladoB):
        self._ladoB = ladoB

    @property
    def ladoC(self):
        return self._ladoC

    @ladoC.setter
    def ladoC(self, ladoC):
        self._ladoC = ladoC

    @abstractmethod
    def get_descripcion(self):
        pass

    @abstractmethod
    def get_superficie(self, base, altura):
        pass

    @abstractmethod
    def dibujate(self):
        pass

class Equilatero(Triangulo):
    def get_descripcion(self):
        return "Soy un triángulo Equilátero"

    def get_superficie(self, base, altura):
        return 0  # Implementa la fórmula para calcular la superficie según tus necesidades

    def dibujate(self):
        pass  # Implementa la lógica para dibujar el triángulo

class Escaleno(Triangulo):
    def get_descripcion(self):
        return "Es un triángulo Escaleno"

    def get_superficie(self, base, altura):
        return 0  # Implementa la fórmula para calcular la superficie según tus necesidades

    def dibujate(self):
        pass  # Implementa la lógica para dibujar el triángulo

class Isosceles(Triangulo):
    def get_descripcion(self):
        return "Es un triángulo Isosceles"

    def get_superficie(self, base, altura):
        return 0  # Implementa la fórmula para calcular la superficie según tus necesidades

    def dibujate(self):
        pass  # Implementa la lógica para dibujar el triángulo
