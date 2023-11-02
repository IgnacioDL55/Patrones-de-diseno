from Tv_Abstract_Factory import TvAbstractFactory
from Plasma import Plasma
from Amarillo import Amarillo 

class FactoryPlasmaAmarillo(TvAbstractFactory):
    def create_color(self):
        return Amarillo()

    def create_tv(self):
        return Plasma()