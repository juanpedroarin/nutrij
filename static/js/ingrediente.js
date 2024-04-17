// Función para agregar un nuevo dropdown de ingredientes
function agregarIngrediente() {
    var contenedor = document.getElementById("ingredientes-container");
    var select = document.createElement("select");
    select.id = "ingredientes"
    select.name="ingredientes[]"

    // Agregar opciones de ingredientes al dropdown
    fetch('/get_dropdown_ingredientes')
        .then(response => response.json())
        .then(opciones =>{
            opciones.forEach(function(ingrediente){
                var option = document.createElement("option");
                option.text = ingrediente[1];
                option.value = ingrediente[0];
                select.add(option);
            });
        })

    contenedor.appendChild(select);
    contenedor.appendChild(document.createElement("br")); // Salto de línea
};