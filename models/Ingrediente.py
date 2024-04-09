class Ingrediente:
    def __init__(self, nombre, unidad, prote):
        self.nombre = nombre
        self.unidad = unidad
        self.prote = prote 

    def __str__(self) -> str:
        return '[[Ingrediente: >>>>> {}, {}, {}]]'.format(self.nombre, self.unidad, self.prote)
