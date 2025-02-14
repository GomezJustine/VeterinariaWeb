from django.shortcuts import render, redirect
from django.contrib import messages
from appVeterinaria.models import ConfiguracionEmpresa, Persona
from django.contrib.auth.hashers import check_password
from base64 import b64encode
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    # Variables para logos
    logo = None
    logo1 = None

    # Obtener los logos de la configuración de la empresa
    configuracion = ConfiguracionEmpresa.objects.first()
    if configuracion:
        if configuracion.logo:
            logo = f"data:image/png;base64,{b64encode(configuracion.logo).decode('utf-8')}"
        if configuracion.logo1:
            logo1 = f"data:image/png;base64,{b64encode(configuracion.logo1).decode('utf-8')}"

    if request.method == 'POST':
        # Capturar los datos del formulario
        cedula = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        # Validar que los campos no estén vacíos
        if not cedula or not password:
            messages.error(request, "Debe ingresar su cédula y contraseña.")
            return render(request, 'autenticador.html', {'logo': logo, 'logo1': logo1})

        # Buscar al usuario en la base de datos
        try:
            usuario = Persona.objects.get(cedula=cedula)
            # Validar la contraseña
            if check_password(password, usuario.contraseña):
                # Credenciales válidas
                request.session['cedula'] = usuario.cedula  # Guardar la cédula en la sesión
                messages.success(request, "Inicio de sesión exitoso.")
                if usuario.rol == 'cliente':
                    return redirect('iniciousuario')  # Redirigir a vista de cliente
                elif usuario.rol == 'administrador':
                    return redirect('inicioadm')  # Redirigir a vista de administrador
            else:
                messages.error(request, "Contraseña incorrecta.")
        except Persona.DoesNotExist:
            messages.error(request, "Usuario no encontrado.")

    # Renderizar el formulario con los logos y mensajes
    return render(request, 'autenticador.html', {'logo': logo, 'logo1': logo1})
