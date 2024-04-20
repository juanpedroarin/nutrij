import psycopg2, os
from dotenv import load_dotenv
from models.Ingrediente import Ingrediente
from models.Receta import Receta

class dbConn:
    def __init__(self):
        load_dotenv()
        self.connData = {
            'dbname': os.getenv("ENV_DB_NAME_PROD"),
            'user': os.getenv("ENV_USER"),
            'host': os.getenv("ENV_HOST"),
            'port': os.getenv("ENV_PORT")
            }

    def execute_query(self, query, data=None):
            conn = psycopg2.connect(**self.connData)
            cur = conn.cursor()
            if data:
                cur.execute(query, data)
            else:
                cur.execute(query)
            try:
                result = cur.fetchall()
            except psycopg2.ProgrammingError as e:
                result = ""
            conn.commit()
            cur.close()
            conn.close()
            return result

# Ingredientes
    def db_crear_ingrediente(self, nombre, unidad, prote):
        query = """INSERT INTO public.ingredientes (nombre, unidad, prote) 
                    VALUES (%s, %s, %s);"""
        data = (nombre, unidad, prote)
        self.execute_query(query, data)
    
    def db_cargar_ingredientes(self):
        query = "SELECT * FROM public.ingredientes"
        result = self.execute_query(query)
        lista_ingredientes = []
        for ingr in result:
            ingrediente = Ingrediente(ingr[0], ingr[1], ingr[2], ingr[3])
            lista_ingredientes.append(ingrediente)
        return lista_ingredientes
    
# Recetas
    def db_crear_receta(self, nombre, descripcion, id_ingredientes):
        query = """INSERT INTO public.recetas(
                    nombre, descripcion)
                    VALUES (%s, %s)
                    RETURNING id;"""
        data = (nombre, descripcion)
        id_receta = self.execute_query(query, data)[0]
        for id_ingr in id_ingredientes:
            query = """INSERT INTO public.receta_ingredientes(
                        id_receta, id_ingrediente)
                        VALUES (%s, %s);"""
            data = (id_receta, id_ingr)
            self.execute_query(query, data)
    
    def db_cargar_recetas(self, lista_ingredientes_sis):
        query = """SELECT id, nombre, descripcion
                    FROM public.recetas;"""
        recetas = self.execute_query(query)
        lista_recetas = []
        for rece in recetas:
            receta = Receta(rece[0], rece[1], rece[2])
            query_receta_ingredientes = """SELECT id_ingrediente
                                            FROM public.receta_ingredientes
                                            WHERE id_receta = %s;"""
            lista_id_ingredientes_receta = self.execute_query(query_receta_ingredientes, (rece[0],))
            ingredientes_receta = []          
            for id_i in lista_id_ingredientes_receta:
                ingrediente_obj =  next((ingrediente for ingrediente in lista_ingredientes_sis if ingrediente.id == id_i[0]), None)
                if ingrediente_obj:
                    ingredientes_receta.append(ingrediente_obj)
            receta.ingredientes = ingredientes_receta
            lista_recetas.append(receta)
        return lista_recetas