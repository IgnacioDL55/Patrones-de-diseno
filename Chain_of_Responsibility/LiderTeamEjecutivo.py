from IAprobador import IAprobador
class LiderTeamEjecutivo(IAprobador):
    def __init__(self):
        self._next = None

    def set_next(self, aprobador):
        self._next = aprobador

    def get_next(self):
        return self._next

    def solicitud_prestamo(self, monto):
        if 10000 < monto <= 50000:
            print("Manejado por Líder del Team Ejecutivo")
        elif self._next:
            self._next.solicitud_prestamo(monto)
