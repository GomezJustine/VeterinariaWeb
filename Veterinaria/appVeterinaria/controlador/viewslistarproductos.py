from django.shortcuts import render
from appVeterinaria.models import ConfiguracionEmpresa, Tbproducto, Persona
from base64 import b64encode

def listar_productos(request):
    logo = None
    nombre_usuario = None  # Variable para guardar el nombre del usuario logueado

    # Obtener logo desde ConfiguracionEmpresa
    configuracion = ConfiguracionEmpresa.objects.first()
    if configuracion and configuracion.logo:
        logo = f"data:image/png;base64,{b64encode(configuracion.logo).decode('utf-8')}"

    # Verificar si el usuario está logueado
    cedula = request.session.get('cedula')
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            nombre_usuario = usuario.nombre  # Extraemos el nombre del usuario logueado
        except Persona.DoesNotExist:
            nombre_usuario = None  # Si no se encuentra, mantenemos None

    # Recuperar todos los productos con su categoría
    productos = Tbproducto.objects.select_related('idCategoria').all()

    # Renderizar el template con los productos
    return render(request, 'listar_productos.html', {
        'logo': logo,
        'productos': productos,
        'nombre_usuario': nombre_usuario,  # Pasar el nombre del usuario al template
    })
