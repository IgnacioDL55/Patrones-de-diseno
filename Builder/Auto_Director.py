from Auto_Builder import AutoBuilder

class AutoDirector:
    def __init__(self):
        self.auto_builder = None

    def construct_auto(self):
        self.auto_builder.crear_auto()
        self.auto_builder.build_marca()
        self.auto_builder.build_modelo()
        self.auto_builder.build_motor()
        self.auto_builder.build_puertas()

    def set_auto_builder(self, auto_builder):
        self.auto_builder = auto_builder

    def get_auto(self):
        return self.auto_builder.get_auto()
