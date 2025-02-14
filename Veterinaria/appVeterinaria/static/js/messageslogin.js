document.addEventListener('DOMContentLoaded', () => {
    // Seleccionar todos los mensajes en el contenedor
    const messages = document.querySelectorAll('.popup-message');

    // Mostrar los mensajes y configurar la eliminación automática
    messages.forEach((message) => {
        // Agregar animación de entrada (opcional)
        message.style.transition = 'opacity 0.5s';
        message.style.opacity = '1';

        // Eliminar después de 5 segundos
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 500); // Esperar la duración de la transición
        }, 5000);
    });
});
