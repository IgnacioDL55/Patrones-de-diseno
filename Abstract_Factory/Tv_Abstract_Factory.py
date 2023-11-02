from abc import ABC, abstractmethod

class TvAbstractFactory(ABC):
    @abstractmethod
    def create_tv(self):
        pass

    @abstractmethod
    def create_color(self):
        pass