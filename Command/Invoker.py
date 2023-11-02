from Command import Command
class Invoker:
    def __init__(self, commander):
        self.commander = commander

    def run(self):
        self.commander.execute()
