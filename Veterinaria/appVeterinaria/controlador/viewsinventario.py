from django.shortcuts import render, redirect
from django.core.files.uploadedfile import InMemoryUploadedFile
from appVeterinaria.models import ConfiguracionEmpresa, Tbproducto, Persona
from base64 import b64encode
from decimal import Decimal

def inventario(request):
    logo = None
    nombre_usuario = None  # Variable para guardar el nombre del usuario logueado

    # Obtener logo desde ConfiguracionEmpresa
    configuracion = ConfiguracionEmpresa.objects.first()
    if configuracion and configuracion.logo:
        logo = f"data:image/png;base64,{b64encode(configuracion.logo).decode('utf-8')}"

    # Obtener productos activos para mostrar en el inventario
    try:
        productos = Tbproducto.objects.filter(activo=True)  # Filtra productos activos
        # Convierte las imágenes en base64 para usarlas en el template
        for producto in productos:
            if producto.imagen:
                producto.imagen = f"data:image/png;base64,{b64encode(producto.imagen).decode('utf-8')}"
    except Exception as e:
        productos = []
        error = f"Error al cargar los productos: {e}"

    # Obtener información del usuario logueado
    cedula = request.session.get('cedula')
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            nombre_usuario = usuario.nombre  # Extraemos el nombre del usuario logueado
        except Persona.DoesNotExist:
            pass

    # Renderizar la plantilla con los datos necesarios
    return render(request, "inventario.html", {
        "logo": logo,
        "productos": productos,  # Pasar los productos al template
        "nombre_usuario": nombre_usuario,  # Pasar el nombre del usuario al template
    })
