from django.shortcuts import render, redirect
from django.contrib import messages
from appVeterinaria.models import ConfiguracionEmpresa, Persona
from base64 import b64encode

def configuracion_empresa(request):
    logo = None
    nombre_usuario = None  # Variable para guardar el nombre del usuario logueado
    configuracion = ConfiguracionEmpresa.objects.first()
    
    if configuracion and configuracion.logo:
        logo = f"data:image/png;base64,{b64encode(configuracion.logo).decode('utf-8')}"
        
    # Obtener el nombre del usuario autenticado
    cedula = request.session.get('cedula')
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            nombre_usuario = usuario.nombre  # Extraemos el nombre del usuario logueado
        except Persona.DoesNotExist:
            pass
        

    if request.method == "POST":
        # Actualizar texto y otros campos
        configuracion.nombre_empresa = request.POST.get('nombre_empresa', configuracion.nombre_empresa)
        configuracion.direccion = request.POST.get('direccion', configuracion.direccion)
        configuracion.telefono = request.POST.get('telefono', configuracion.telefono)
        configuracion.email = request.POST.get('email', configuracion.email)
        configuracion.descripcion = request.POST.get('descripcion', configuracion.descripcion)
        configuracion.texto_footer = request.POST.get('texto_footer', configuracion.texto_footer)

        # Manejar logos
        if request.FILES.get('logo'):
            configuracion.logo = request.FILES['logo'].read()
        if request.FILES.get('logo1'):
            configuracion.logo1 = request.FILES['logo1'].read()

        # Manejar banners
        for i in range(6):
            banner_key = f'banner{i}' if i != 0 else 'banner'
            if request.FILES.get(banner_key):
                setattr(configuracion, banner_key, request.FILES[banner_key].read())

        configuracion.save()
        messages.success(request, "Configuración actualizada exitosamente.")
        return redirect('ajustes')

    return render(request, "ajustes.html", {
        "configuracion": configuracion,
        "logo": logo,
        "nombre_usuario": nombre_usuario,  # Pasar el nombre del usuario al template
    })
