from Auto import Auto

class AutoBuilder:
    def __init__(self):
        self.auto = None

    def get_auto(self):
        return self.auto

    def crear_auto(self):
        self.auto = Auto()

    def build_motor(self):
        pass

    def build_modelo(self):
        pass

    def build_marca(self):
        pass

    def build_puertas(self):
        pass
