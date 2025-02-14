// Abrir el modal
function openModal() {
    document.getElementById("editModal").style.display = "block";
}

// Cerrar el modal
function closeModal() {
    document.getElementById("editModal").style.display = "none";
}

// Cerrar el modal si se hace clic fuera del contenido
window.onclick = function (event) {
    const modal = document.getElementById("editModal");
    if (event.target === modal) {
        closeModal();
    }
};
