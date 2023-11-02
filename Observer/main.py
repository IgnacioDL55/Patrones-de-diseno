from AlarmaLibro import AlarmaLibro
from Administracion import Administracion
from Stock import Stock
from Compras import Compras
from Libro import Libro
from Biblioteca import Biblioteca

if __name__ == "__main__":

    alarma = AlarmaLibro()
    alarma.attach(Administracion())
    alarma.attach(Stock())
    alarma.attach(Compras())

    l1 = Libro("Bueno", "Design Pattern")
    l1.set_estado("MALO")

    b1 = Biblioteca(alarma)
    b1.devuelve_libro(l1)