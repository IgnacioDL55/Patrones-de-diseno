from IlibroMalEstado import ILibroMalEstado  # Asegúrate de importar la interfaz ILibroMalEstado correctamente

class Stock(ILibroMalEstado):
    def update(self):
        print("Stock:El libro roto salió de stock")
