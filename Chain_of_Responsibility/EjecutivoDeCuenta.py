from IAprobador import IAprobador
class EjecutivoDeCuenta(IAprobador):
    def __init__(self):
        self._next = None

    def set_next(self, aprobador):
        self._next = aprobador

    def get_next(self):
        return self._next

    def solicitud_prestamo(self, monto):
        if monto <= 10000:
            print("Manejado por Ejecutivo de Cuenta")
        elif self._next:
            self._next.solicitud_prestamo(monto)
