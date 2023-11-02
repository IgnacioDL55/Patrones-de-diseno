from Triangulo import Triangulo, Equilatero, Escaleno, Isosceles
from Triangulo_Factory import TrianguloFactory

def main():
    metodo = TrianguloFactory()
    triangulo = metodo.create_triangulo(15, 10, 10)

    print(triangulo.get_descripcion())

if __name__ == "__main__":
    main()
