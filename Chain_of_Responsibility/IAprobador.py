from abc import ABC, abstractmethod

class IAprobador(ABC):
    @abstractmethod
    def set_next(self, aprobador):
        pass

    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def solicitud_prestamo(self, monto):
        pass

