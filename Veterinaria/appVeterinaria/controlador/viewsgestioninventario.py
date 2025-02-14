from base64 import b64encode
from django.shortcuts import render
from appVeterinaria.models import ConfiguracionEmpresa, Persona

def gestion_productos(request):
    # Inicializar variable para el logo
    logo = None
    nombre_usuario = None  # Variable para guardar el nombre del usuario logueado


    # Cargar el logo desde la base de datos
    configuracion = ConfiguracionEmpresa.objects.first()

    if configuracion and configuracion.logo:
        # Convertir el logo a base64
        logo = b64encode(configuracion.logo).decode('utf-8')
        
        
    cedula = request.session.get('cedula')
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            nombre_usuario = usuario.nombre  # Extraemos el nombre del usuario logueado
        except Persona.DoesNotExist:
            pass

    # Renderizar la plantilla
    return render(request, "administrador.html", {
        "logo": logo,
        "nombre_usuario": nombre_usuario,  # Pasar el nombre del usuario al template
    })
