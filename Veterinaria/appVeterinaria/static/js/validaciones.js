// Validación del campo ID de Producto
document.getElementById("productID").addEventListener("input", function(event) {
    // Permitir solo números en el campo de ID
    this.value = this.value.replace(/[^0-9]/g, '');
});

// Validación del campo Nombre del Producto
document.getElementById("productName").addEventListener("input", function(event) {
    // Permitir solo letras y espacios en el campo de Nombre del Producto
    this.value = this.value.replace(/[^A-Za-z\s]/g, '');
});
