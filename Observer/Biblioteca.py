class Biblioteca:
    def __init__(self, alarma_libro):
        self.alarma_libro = alarma_libro

    def devuelve_libro(self, libro):
        if libro.get_estado() == "MALO":
            self.alarma_libro.notify_observer()