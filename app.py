from flask import Flask, render_template, request
from models.Ingrediente import Ingrediente

app = Flask('__name__')

@app.route('/crear_ingrediente', methods=['GET', 'POST'])
def crear_ingrediente():
    if request.method == 'GET':
        return render_template('ingrediente.html')
    elif request.method == 'POST':
        nombre = request.form['nombre']
        unidad = request.form['unidad']
        prote = request.form['prote']
        nuevo_ingrediente = Ingrediente(nombre, unidad, prote)
        print(str(nuevo_ingrediente))
        return str(nuevo_ingrediente)


if __name__ == '__main__':
    app.run(debug=True)
