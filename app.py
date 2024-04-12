from flask import Flask, render_template, request
from models.Ingrediente import Ingrediente
from database.dbconn import dbConn

app = Flask('__name__')

#Inicializar variables
dbconn = dbConn()

@app.route('/crear_ingrediente', methods=['GET', 'POST'])
def crear_ingrediente():
    if request.method == 'GET':
        return render_template('ingrediente.html')
    elif request.method == 'POST':
        nombre = request.form['nombre']
        unidad = request.form['unidad']
        prote = request.form['prote']
        dbconn.db_crear_ingrediente(nombre, unidad, prote)
        return "Ingdediente creado"
    
@app.route('/crear_receta', methods=['GET', 'POST'])
def crear_receta():
    if request.method == 'GET':
        return render_template('receta.html')
    elif request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        id_ingredientes = request.form.getlist('ingredientes[]')
        dbconn.db_crear_receta(nombre, descripcion, id_ingredientes)
        return "Receta creada"
    
@app.route('/get_dropdown_ingredientes', methods=['GET'])
def get_dropdown_ingredientes():
    opciones = dbconn.db_cargar_ingredientes()
    return opciones


if __name__ == '__main__':
    app.run(debug=True)
