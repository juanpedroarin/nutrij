
class Ingrediente:
    def __init__(self, id, nombre, unidad, prote):
        self.id = id
        self.nombre = nombre
        self.unidad = unidad
        self.prote = prote

    def __str__(self) -> str:
        return '[Ing: {}, {}, {}]'.format(self.nombre, self.unidad, self.prote)
