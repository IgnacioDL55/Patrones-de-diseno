from Auto_Builder import AutoBuilder
from Motor import Motor

class FiatBuilder(AutoBuilder):
    def build_marca(self):
        self.auto.set_marca("Fiat")

    def build_modelo(self):
        self.auto.set_modelo("Pulse")

    def build_motor(self):
        motor = Motor()
        motor.set_numero(232323)
        motor.set_potencia("23 hp")
        self.auto.set_motor(motor)

    def build_puertas(self):
        self.auto.set_cantidad_de_puertas(2)
