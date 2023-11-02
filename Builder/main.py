from Auto_Director import AutoDirector
from Fiat_Builder import FiatBuilder
from Ford_Builder import FordBuilder

def main():
    director_fiat = AutoDirector()
    fiat_builder = FiatBuilder()

    director_fiat.set_auto_builder(fiat_builder)
    director_fiat.construct_auto()
    auto_fiat = director_fiat.get_auto()
    print("Fiat - Marca:", auto_fiat.get_marca())
    print("Fiat - Modelo:", auto_fiat.get_modelo())

    director_ford = AutoDirector()
    ford_builder = FordBuilder()

    director_ford.set_auto_builder(ford_builder)
    director_ford.construct_auto()
    auto_ford = director_ford.get_auto()
    print("Ford - Marca:", auto_ford.get_marca())
    print("Ford - Modelo:", auto_ford.get_modelo())

if __name__ == "__main__":
    main()
