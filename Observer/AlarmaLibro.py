from Subject import Subject

class AlarmaLibro(Subject):
    def __init__(self):
        self.observadores = []

    def attach(self, observador):
        self.observadores.append(observador)

    def detach(self, observador):
        self.observadores.remove(observador)

    def notify_observer(self):
        for observer in self.observadores:
            observer.update()
