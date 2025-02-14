from django.shortcuts import render
from django.contrib import messages
from appVeterinaria.models import ConfiguracionEmpresa, Persona
from base64 import b64encode

def perfil(request):
    # Inicialización de variables
    logo = None
    nombre_usuario = None  # Guardar el nombre del usuario logueado
    usuario = None  # Datos del usuario logueado    
    rol = None  # Variable para almacenar el rol del usuario



    # Obtener el logo desde ConfiguracionEmpresa (misma lógica que en desactivar_producto)
    configuracion = ConfiguracionEmpresa.objects.first()
    if configuracion and configuracion.logo:
        logo = f"data:image/png;base64,{b64encode(configuracion.logo).decode('utf-8')}"

    # Obtener información del usuario autenticado
    cedula = request.session.get('cedula')  # Obtener la cédula desde la sesión
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            nombre_usuario = usuario.nombre  # Guardar el nombre del usuario
            rol = usuario.rol  # Extraer el rol del usuario
        except Persona.DoesNotExist:
            pass
        
    # Manejar los datos enviados por el formulario
    if request.method == "POST":
        nombre = request.POST.get('nombre', usuario.nombre)
        email = request.POST.get('email', usuario.email)
        nueva_contraseña = request.POST.get('nueva_contraseña', None)
        confirmar_contraseña = request.POST.get('confirmar_contraseña', None)

        # Validar contraseñas si se proporciona una nueva
        if nueva_contraseña or confirmar_contraseña:
            if nueva_contraseña != confirmar_contraseña:
                messages.error(request, "Las contraseñas no coinciden.")
                return render(request, "perfil.html", {
                    "logo": logo,
                    "usuario": usuario,
                    "nombre_usuario": nombre_usuario,
                    "rol": rol,  # Asegúrate de incluir el rol aquí
                    "error": "Las contraseñas no coinciden.",
                })

            usuario.contraseña = nueva_contraseña  # Cambiar contraseña

        # Actualizar los campos
        usuario.nombre = nombre
        usuario.email = email
        usuario.save()
        
        messages.success(request, "¡Cambios realizados con éxito!")
        return render(request, "perfil.html", {
            "logo": logo,
            "usuario": usuario,
            "nombre_usuario": nombre_usuario,
            "rol": rol,  # Pasar el rol
        })

    # Renderizar el template
    return render(request, "perfil.html", {
        "logo": logo,
        "nombre_usuario": nombre_usuario, 
        "usuario": usuario,  
        "rol": rol,  # Pasar el rol al template
    })
