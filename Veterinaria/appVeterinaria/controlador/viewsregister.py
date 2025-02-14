from django.shortcuts import render, redirect  # Para renderizar plantillas y redirigir vistas
from django.contrib import messages  # Para manejar mensajes de éxito y error en la plantilla
from appVeterinaria.models import ConfiguracionEmpresa, Persona  # Modelos necesarios
from base64 import b64encode  # Para convertir el logo en formato base64 y mostrarlo en la plantilla
from django.views.decorators.csrf import csrf_exempt  # Deshabilita la protección CSRF para pruebas específicas (no recomendado en producción)
from django.contrib.auth.hashers import make_password  # Para encriptar contraseñas antes de guardarlas
from django.core.validators import validate_email  # Para validar que el email tenga un formato válido
from django.core.exceptions import ValidationError  # Para manejar errores al validar el email

@csrf_exempt
def register_user(request):
    SECURITY_CODE = "12345"  # Código de seguridad predefinido para administrador
    logo = None
    logo1 = None

    # Obtener los logos de la tabla ConfiguracionEmpresa
    configuracion = ConfiguracionEmpresa.objects.first()  # Obtiene la primera configuración
    if configuracion:
        # Convertir los logos a base64 para que puedan ser renderizados en el HTML
        if configuracion.logo:
            logo = f"data:image/png;base64,{b64encode(configuracion.logo).decode('utf-8')}"
        if configuracion.logo1:
            logo1 = f"data:image/png;base64,{b64encode(configuracion.logo1).decode('utf-8')}"

    if request.method == 'POST':  # Procesar los datos solo si el método es POST
        # Capturar datos enviados por el formulario
        cedula = request.POST.get('cedula', '').strip()  # Captura la cédula
        nombre = request.POST.get('nombre', '').strip()  # Captura el nombre
        email = request.POST.get('email', '').strip()  # Captura el email
        password = request.POST.get('password', '').strip()  # Captura la contraseña
        role = request.POST.get('role', '').strip()  # Captura el rol del usuario
        security_code = request.POST.get('security_code', '').strip()  # Captura el código de seguridad

        # Lista para almacenar errores de validación
        errores = []

        # **Validaciones**:
        if not cedula.isdigit() or len(cedula) < 5:
            errores.append("La cédula debe ser numérica y tener al menos 5 dígitos.")
        elif Persona.objects.filter(cedula=cedula).exists():
            errores.append("La cédula ya está registrada.")

        if not nombre or len(nombre) < 3:
            errores.append("El nombre debe tener al menos 3 caracteres.")

        try:
            validate_email(email)
        except ValidationError:
            errores.append("El correo electrónico no tiene un formato válido.")
        else:
            if Persona.objects.filter(email=email).exists():
                errores.append("El correo electrónico ya está registrado.")

        if not password or len(password) < 8:
            errores.append("La contraseña debe tener al menos 8 caracteres.")

        if role not in ['cliente', 'administrador']:
            errores.append("El tipo de usuario debe ser 'cliente' o 'administrador'.")

        if role == "administrador" and security_code != SECURITY_CODE:
            errores.append("El código de seguridad para administrador es incorrecto.")

        if errores:
            for error in errores:
                messages.error(request, error)
            return render(request, 'register.html', {'logo': logo, 'logo1': logo1})

        try:
            nuevo_usuario = Persona.objects.create(
                cedula=int(cedula),
                nombre=nombre,
                email=email,
                contraseña=make_password(password),
                rol=role
            )
            messages.success(request, "Usuario registrado correctamente.")
            return redirect('autenticador.html')
        except Exception as e:
            messages.error(request, f"Error al registrar el usuario: {str(e)}")
            return render(request, 'register.html', {'logo': logo, 'logo1': logo1})

    # Si es método GET, renderiza el formulario
    return render(request, 'register.html', {'logo': logo, 'logo1': logo1})
