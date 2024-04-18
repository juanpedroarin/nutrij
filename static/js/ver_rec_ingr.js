//Agregar los ingredientes y recetas

function verRecetas() {
    var contenedor = document.getElementById("recetas-container")

    fetch('/get?tipo=recetas')
        .then(response => response.json())
        .then(recetas => {
            recetas.forEach(receta => {
                var a = document.createElement('a')
                a.text = receta.nombre + " - " + receta.ingredientes
                contenedor.appendChild(a)
                contenedor.appendChild(document.createElement('br'))
            })
        })
}

function verIngredientes() {
    var contenedor = document.getElementById("ingredientes-container")
    
    fetch('/get?tipo=ingredientes')
        .then(response => response.json())
        .then(ingredientes =>{
            ingredientes.forEach(element => {
                var a = document.createElement("a");
                a.text = element.nombre
                contenedor.appendChild(a)
                contenedor.appendChild(document.createElement("br")); // Salto de línea
            });
        })
}

verRecetas();
verIngredientes();