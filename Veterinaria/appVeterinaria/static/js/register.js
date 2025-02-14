// Función para mostrar la ventana emergente de éxito
function showSuccessPopup(event) {
    event.preventDefault(); // Evita que el formulario se envíe de inmediato

    // Verificar si las variables están definidas
    if (!registerUrl || !csrfToken) {
        console.error("registerUrl o csrfToken no están definidos.");
        return;
    }

    // Enviar los datos del formulario al servidor para registro
    const formData = new FormData(document.querySelector('.register-form'));

    fetch(registerUrl, {  // URL del endpoint de registro
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': csrfToken  // Token CSRF para proteger la solicitud
        }
    })
    .then(response => {
        if (response.ok) {
            console.log("Registro exitoso.");
            // Si el registro fue exitoso, muestra el popup de éxito
            document.getElementById('successPopup').style.display = 'flex';
        } else {
            // Manejar errores en la respuesta
            response.json().then(data => {
                alert(data.error || "Ocurrió un error durante el registro.");
            });
        }
    })
    .catch(error => console.error('Error:', error));
}

// Función para cerrar la ventana emergente y redirigir al usuario
function closePopupAndRedirect() {
    // Oculta la ventana emergente
    document.getElementById('successPopup').style.display = 'none';

    // Redirige a la página de inicio de sesión
    window.location.href = loginUrl;  // Redirige a loginUrl
}

// Mostrar el campo de código de seguridad solo si el rol es "administrador"
document.addEventListener("DOMContentLoaded", function() {
    const roleSelect = document.getElementById("role");
    const securityCodeField = document.getElementById("security_code");

    roleSelect.addEventListener("change", function() {
        if (roleSelect.value === "administrador") {
            securityCodeField.style.display = "block";
        } else {
            securityCodeField.style.display = "none";
        }
    });
});

// Escucha el evento de envío del formulario para manejar el registro
document.querySelector('.register-form').addEventListener('submit', showSuccessPopup);

