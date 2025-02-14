document.getElementById("deleteProductForm").addEventListener("submit", function(event) {
    const confirmation = confirm("¿Estás seguro de que deseas Desactivar este producto?");
    if (!confirmation) {
        event.preventDefault();
    }
});

