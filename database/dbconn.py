import psycopg2

class dbConn:
    def __init__(self):
        self.connData = {
            'dbname': 'NutrijDB',
            'user': 'postgres',
            'host': 'localhost',
            'port': '5432'
            }

    def execute_insert_query(self, query, data=None):
            conn = psycopg2.connect(**self.connData)
            cur = conn.cursor()
            if data:
                cur.execute(query, data)
            else:
                cur.execute(query)
            try:
                result = cur.fetchone()
            except psycopg2.ProgrammingError as e:
                result = ""
            conn.commit()
            cur.close()
            conn.close()
            return result

    def db_crear_ingrediente(self, nombre, unidad, prote):
        query = """INSERT INTO public.ingredientes (nombre, unidad, prote) 
                    VALUES (%s, %s, %s);"""
        data = (nombre, unidad, prote)
        self.execute_insert_query(query, data)

    def db_cargar_ingredientes(self):
        conn = psycopg2.connect(**self.connData) ##'**' transforma el dicc en cadena DSN
        cur = conn.cursor()

        cur.execute("SELECT id, nombre FROM public.ingredientes")
        ingredientes = cur.fetchall()
        print(str(ingredientes))

        conn.commit()
        cur.close()
        conn.close()
        return ingredientes
    
    def db_crear_receta(self, nombre, descripcion, id_ingredientes):
        query = """INSERT INTO public.recetas(
                    nombre, descripcion)
                    VALUES (%s, %s)
                    RETURNING id;"""
        data = (nombre, descripcion)
        id_receta = self.execute_insert_query(query, data)
        for id_ingr in id_ingredientes:
            query = """INSERT INTO public.receta_ingredientes(
                        id_receta, id_ingrediente)
                        VALUES (%s, %s);"""
            data = (id_receta, id_ingr)
            self.execute_insert_query(query, data)