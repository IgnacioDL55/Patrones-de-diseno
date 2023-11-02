from Factory_Lcd_Azul import FactoryLcdAzul  # Asegúrate de importar la clase FactoryLcdAzul
from Factory_Plasma_Amarillo import FactoryPlasmaAmarillo  # Asegúrate de importar la clase FactoryPlasmaAmarillo
from Ensamblaje_tv import EnsamblajeTv  # Asegúrate de importar la clase EnsamblajeTv


def main():
    fabrica1 = FactoryLcdAzul()
    ensamble1 = EnsamblajeTv(fabrica1)

    fabrica2 = FactoryPlasmaAmarillo()
    ensamble2 = EnsamblajeTv(fabrica2)

if __name__ == "__main__":
    main()
