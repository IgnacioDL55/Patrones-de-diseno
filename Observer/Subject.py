from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def attach(self, observador):
        pass

    @abstractmethod
    def detach(self, observador):
        pass

    @abstractmethod
    def notify_observer(self):
        pass
