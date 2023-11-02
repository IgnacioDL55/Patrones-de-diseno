from Auto_Builder import AutoBuilder
from Motor import Motor

class FordBuilder(AutoBuilder):
    def build_marca(self):
        self.auto.set_marca("Ford")

    def build_modelo(self):
        self.auto.set_modelo("Kuga")

    def build_motor(self):
        motor = Motor()
        motor.set_numero(21212)
        motor.set_potencia("20 hp")
        self.auto.set_motor(motor)

    def build_puertas(self):
        self.auto.set_cantidad_de_puertas(4)
