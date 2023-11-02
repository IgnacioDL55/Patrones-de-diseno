from IAprobador import IAprobador
class Gerente(IAprobador):
    def __init__(self):
        self._next = None

    def set_next(self, aprobador):
        self._next = aprobador

    def get_next(self):
        return self._next

    def solicitud_prestamo(self, monto):
        if 50000 < monto <= 100000:
            print("Manejado por Gerente")
        elif self._next:
            self._next.solicitud_prestamo(monto)
