// Mostrar el modal al hacer clic en "Gestionar Banners"
document.getElementById('banners-button').addEventListener('click', () => {
    document.getElementById('gestionar-banners-modal').style.display = 'block';
});

// Cerrar el modal cuando se haga clic en el botón "Salir"
function cerrarModal() {
    document.getElementById('gestionar-banners-modal').style.display = 'none';
}

// Previsualizar las imágenes seleccionadas
const bannerInputs = document.querySelectorAll('input[type="file"]');

bannerInputs.forEach(input => {
    input.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            console.log(`Archivo seleccionado para ${event.target.id}: ${file.name}`);
        }
    });
});
