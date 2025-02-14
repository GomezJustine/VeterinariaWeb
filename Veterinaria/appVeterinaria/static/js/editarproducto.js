// Validación de ID del Producto (solo números)
document.getElementById("productID").addEventListener("input", function(event) {
    this.value = this.value.replace(/[^0-9]/g, ''); // Permitir solo números
});

// Validación de cantidad (sin valores negativos)
document.getElementById("productQuantity").addEventListener("input", function(event) {
    if (parseInt(this.value) < 0) {
        alert("No se permiten valores negativos en el stock.");
        this.value = "";
    }
});

// Validación de precio (múltiplo de 100)
document.getElementById("productPrice").addEventListener("input", function(event) {
    if (this.value % 100 !== 0) {
        alert("El precio debe ser un múltiplo de 100.");
        this.value = Math.ceil(this.value / 100) * 100; // Redondear al múltiplo más cercano
    }
});
