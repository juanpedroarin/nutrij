class Receta:
    def __init__(self, id, nombre, descripcion, ingredientes=[]):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.ingredientes = ingredientes

    def __str__(self) -> str:
        rece =  "[RECETA {}:, {} ".format(self.id, self.nombre)+", ING: "+str(len(self.ingredientes))
        for ingr in self.ingredientes:
            rece += "({})".format(ingr)
        rece += "]"
        return rece