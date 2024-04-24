import os, random
from utils.dbconn import dbConn

dbconn = dbConn()
dbconn.connData = {
        'dbname': os.getenv("ENV_DB_NAME_TEST"),
        'user': os.getenv("ENV_USER"),
        'host': os.getenv("ENV_HOST"),
        'port': os.getenv("ENV_PORT")
        }

def test_crear_ingrediente():
    
    numero_random = random.randint(1, 1000)
    nombre = 'test_ingr_'+str(numero_random)
    unidad = 'unidad_ingr_'+str(numero_random)
    prote = numero_random
    dbconn.db_crear_ingrediente(nombre, unidad, prote)
    ingredientes = dbconn.db_cargar_ingredientes()
    nuevo = ingredientes.pop()
    assert nuevo.nombre == nombre
    assert nuevo.unidad == unidad
    assert nuevo.prote == prote

def test_crear_receta():
    numero_random = random.randint(1, 1000)
    dbconn.db_crear_ingrediente('ingrediente1_'+str(numero_random), 'unidad1', 1)
    dbconn.db_crear_ingrediente('ingrediente2_'+str(numero_random), 'unidad2', 2)
    dbconn.db_crear_ingrediente('ingrediente3_'+str(numero_random), 'unidad3', 3)
    ingredientes = dbconn.db_cargar_ingredientes()
    ingr_receta = ingredientes[-3:]
    nombre = 'test_receta_'+str(numero_random)
    descripcion = 'test_receta_'+str(numero_random)
    dbconn.db_crear_receta(nombre, descripcion, [ingrediente.id for ingrediente in ingr_receta])
    recetas = dbconn.db_cargar_recetas(ingredientes)
    nueva = recetas.pop()
    assert nueva.nombre == nombre
    assert nueva.descripcion == descripcion
    assert nueva.ingredientes == ingr_receta