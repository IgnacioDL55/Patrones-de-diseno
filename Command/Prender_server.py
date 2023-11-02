from Command import Command

class PrendeServer(Command):
    def __init__(self, servidor):
        self.servidor = servidor

    def execute(self):
        self.servidor.prendete()
        self.servidor.conectate()
        self.servidor.verifica_conexion()
        self.servidor.guarda_log()
        self.servidor.cierra_conexion()
