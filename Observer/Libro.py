class Libro:
    def __init__(self, estado="", titulo=""):
        self.estado = estado
        self.titulo = titulo

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo
