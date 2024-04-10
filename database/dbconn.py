import psycopg2

class dbConn:
    def __init__(self):
        self.connData = {
            'dbname': 'NutrijDB',
            'user': 'postgres',
            'host': 'localhost',
            'port': '5432'
            }
        
    def db_crear_ingrediente(self, nombre, unidad, prote):
        conn = psycopg2.connect(**self.connData) ##'**' transforma el dicc en cadena DSN
        cur = conn.cursor()
        cur.execute("""INSERT INTO public.ingredientes (nombre, unidad, prote) 
                    VALUES (%s, %s, %s);""", (nombre, unidad, prote))
        conn.commit()
        cur.close()
        conn.close()
