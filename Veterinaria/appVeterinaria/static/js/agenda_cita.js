// mensaje.js
document.addEventListener("DOMContentLoaded", () => {
    // Función para mostrar el mensaje de éxito
    function mostrarMensajeExito() {
        // Crear el contenedor del mensaje
        const contenedor = document.createElement("div");
        contenedor.id = "mensajeExito";
        contenedor.style.position = "fixed";
        contenedor.style.top = "50%";
        contenedor.style.left = "50%";
        contenedor.style.transform = "translate(-50%, -50%)";
        contenedor.style.backgroundColor = "rgba(0, 255, 0, 0.9)";
        contenedor.style.color = "#fff";
        contenedor.style.padding = "20px 40px";
        contenedor.style.borderRadius = "10px";
        contenedor.style.boxShadow = "0px 4px 6px rgba(0, 0, 0, 0.3)";
        contenedor.style.zIndex = "1000";
        contenedor.style.textAlign = "center";

        // Crear el texto del mensaje
        const mensaje = document.createElement("p");
        mensaje.innerText = "Cita registrada exitosamente!";
        mensaje.style.marginBottom = "20px";
        mensaje.style.fontSize = "18px";
        mensaje.style.fontWeight = "bold";

        // Botón de aceptar
        const botonAceptar = document.createElement("button");
        botonAceptar.innerText = "Aceptar";
        botonAceptar.style.padding = "10px 20px";
        botonAceptar.style.border = "none";
        botonAceptar.style.borderRadius = "5px";
        botonAceptar.style.backgroundColor = "#007BFF";
        botonAceptar.style.color = "#fff";
        botonAceptar.style.cursor = "pointer";
        botonAceptar.style.fontSize = "16px";
        botonAceptar.style.fontWeight = "bold";

        // Evento para cerrar el mensaje
        botonAceptar.addEventListener("click", () => {
            document.body.removeChild(contenedor);
        });

        // Ensamblar los elementos
        contenedor.appendChild(mensaje);
        contenedor.appendChild(botonAceptar);
        document.body.appendChild(contenedor);
    }

    // Detectar si se muestra el mensaje de éxito desde el backend
    const mensajeExito = document.getElementById("mensajeExitoTrigger");
    if (mensajeExito) {
        mostrarMensajeExito();
    }
});
