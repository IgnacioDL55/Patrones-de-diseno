from Tv_Abstract_Factory import TvAbstractFactory


class EnsamblajeTv:
    def __init__(self, factory: TvAbstractFactory):
        color = factory.create_color()
        tv = factory.create_tv()
        color.colorea(tv)
