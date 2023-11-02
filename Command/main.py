# main.py
from Prender_server import PrendeServer
from Brasil_Server import BrasilServer
from Invoker import Invoker

def main():
    commander = PrendeServer(BrasilServer())
    server_admin = Invoker(commander)
    server_admin.run()

if __name__ == "__main__":
    main()
