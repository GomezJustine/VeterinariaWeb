// Formatear el precio mientras se escribe
function formatPrice(input) {
    let value = input.value.replace(/\D/g, ""); // Eliminar caracteres no numéricos
    input.value = new Intl.NumberFormat("es-CO").format(value); // Aplicar formato colombiano
}

// Validación del nombre del producto (solo letras y espacios)
document.getElementById("productName").addEventListener("input", function () {
    this.value = this.value.replace(/[^A-Za-z\s]/g, ''); // Solo permite letras y espacios
});

// Validación del formulario antes de enviar
document.getElementById("addProductForm").addEventListener("submit", function (event) {
    const productName = document.getElementById("productName");
    if (!/^[A-Za-z\s]+$/.test(productName.value)) {
        alert("El Nombre del Producto solo debe contener letras y espacios.");
        productName.focus();
        event.preventDefault(); // Evita que se envíe el formulario si no cumple
    }
});
