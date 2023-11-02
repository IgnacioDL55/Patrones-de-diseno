from Tv_Abstract_Factory import TvAbstractFactory
from LCD import LCD
from Azul import Azul

class FactoryLcdAzul(TvAbstractFactory):
    def create_color(self):
        return Azul()

    def create_tv(self):
        return LCD()