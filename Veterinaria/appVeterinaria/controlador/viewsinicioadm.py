from base64 import b64encode
from django.shortcuts import render
from appVeterinaria.models import ConfiguracionEmpresa, Persona

def inicio_administrador(request):
    # Variables inicializadas
    logo = None
    logo1 = None
    banners = []
    descripcion = ""
    direccion = ""
    telefono = ""
    email = ""
    texto_footer = ""
    nombre_usuario = None  # Variable para guardar el nombre del usuario logueado


    configuracion = ConfiguracionEmpresa.objects.first()

    if configuracion:
        if configuracion.logo:
            logo = b64encode(configuracion.logo).decode('utf-8')
        if configuracion.logo1:
            logo1 = b64encode(configuracion.logo1).decode('utf-8')

        banner_fields = [
            configuracion.banner, 
            configuracion.banner1, 
            configuracion.banner2, 
            configuracion.banner3, 
            configuracion.banner4, 
            configuracion.banner5, 
        ]
        banners = [
            b64encode(banner).decode('utf-8') for banner in banner_fields if banner
        ]
            # Obtener textos
        descripcion = configuracion.descripcion
        direccion = configuracion.direccion
        telefono = configuracion.telefono
        email = configuracion.email
        texto_footer = configuracion.texto_footer
        
    cedula = request.session.get('cedula')
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            nombre_usuario = usuario.nombre  # Extraemos el nombre del usuario logueado
        except Persona.DoesNotExist:
            pass

    # Verificar en consola los datos que se envían al template
    print("Logo:", logo)
    print("Logo1:", logo1)
    print("Banners:", banners)


    # Renderizar la plantilla con los datos procesados
    return render(request, "inicioadm.html", {
        "logo": logo,
        "logo1": logo1,
        "banners": banners,
        "descripcion": descripcion,
        "direccion": direccion,
        "telefono": telefono,
        "email": email,
        "texto_footer": texto_footer,
        "nombre_usuario": nombre_usuario,  # Pasar el nombre del usuario al template
    })
