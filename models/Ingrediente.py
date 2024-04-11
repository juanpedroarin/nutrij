from database.dbconn import dbConn


class Ingrediente:
    def __init__(self, nombre, unidad, prote):
        self.nombre = nombre
        self.unidad = unidad
        self.prote = prote 

    def cargar_ingredientes_dropdown():
        conn = dbConn()
        ingredientes_precargados = conn.db_cargar_ingredientes()
        opciones = [(ingrediente.id, ingrediente.nombre) for ingrediente in ingredientes_precargados ]
        return opciones

    def __str__(self) -> str:
        return '[[Ingrediente: >>>>> {}, {}, {}]]'.format(self.nombre, self.unidad, self.prote)
