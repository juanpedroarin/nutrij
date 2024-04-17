from flask import Flask, render_template, request, jsonify
from utils.dbconn import dbConn

app = Flask('__name__')

# Inicializar variables
dbconn = dbConn()
ingredientes = dbconn.db_cargar_ingredientes()
recetas = dbconn.db_cargar_recetas(ingredientes)

@app.route('/')
def index():
    return render_template('index.html')

# Ruta estática para servir archivos JavaScript
@app.route('/static/js/<path:path>')
def serve_static_js(path):
    return app.send_static_file(f'js/{path}')

# Creadores
@app.route('/crear_ingrediente', methods=['GET', 'POST'])
def crear_ingrediente():
    if request.method == 'GET':
        return render_template('ingrediente.html')
    elif request.method == 'POST':
        nombre = request.form['nombre']
        unidad = request.form['unidad']
        prote = request.form['prote']
        dbconn.db_crear_ingrediente(nombre, unidad, prote)
        global ingredientes
        ingredientes = dbconn.db_cargar_ingredientes()
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
    
# Veedores
@app.route('/ver')
def ver():
    return render_template('ver.html')

# Getters
@app.route('/get', methods=['GET'])
def get():
    tipo = request.args.get('tipo')
    if tipo == 'ingredientes':
        ingredientes_dict = [ingrediente.__dict__ for ingrediente in ingredientes]
        return jsonify(ingredientes_dict)
    elif tipo == 'recetas':
        recetas_dict = [receta.__dict__ for receta in recetas]
        return jsonify(recetas_dict)
    

# Otras
@app.route('/get_dropdown_ingredientes', methods=['GET'])
def get_dropdown_ingredientes():
    opciones = [(ingr.id, ingr.nombre) for ingr in ingredientes]
    return opciones


if __name__ == '__main__':
    app.run(debug=True)
