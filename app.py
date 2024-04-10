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


if __name__ == '__main__':
    app.run(debug=True)
