from Color import Color

class Amarillo(Color):
    def __init__(self):
        super().__init__()
        self.es_primario = True

    def is_es_primario(self):
        return self.es_primario

    def set_es_primario(self, es_primario):
        self.es_primario = es_primario

    def colorea(self, tv):
        print(f"Pintando de amarillo el {tv.get_descripcion()}")