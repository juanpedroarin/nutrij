//Agregar los ingredientes
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

verIngredientes();