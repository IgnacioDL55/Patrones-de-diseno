from abc import ABC, abstractmethod
from Triangulo import Equilatero,Escaleno,Isosceles

class TrianguloFactoryMethod(ABC):
    @abstractmethod
    def create_triangulo(self, ladoA, ladoB, ladoC):
        pass

class TrianguloFactory(TrianguloFactoryMethod):
    def create_triangulo(self, ladoA, ladoB, ladoC):
        if ladoA == ladoB == ladoC:
            return Equilatero(ladoA, ladoB, ladoC)
        elif ladoA != ladoB != ladoC != ladoA:
            return Escaleno(ladoA, ladoB, ladoC)
        else:
            return Isosceles(ladoA, ladoB, ladoC)
