from django.shortcuts import render, get_object_or_404
from appVeterinaria.models import Tbproducto, ConfiguracionEmpresa, Persona
from base64 import b64encode

def detalle_producto(request, producto_id):
    # Obtener el producto
    producto = get_object_or_404(Tbproducto, id=producto_id)
    logo = None
    configuracion = ConfiguracionEmpresa.objects.first()
    
    if configuracion and configuracion.logo:
        logo = f"data:image/png;base64,{b64encode(configuracion.logo).decode('utf-8')}"
        
    # Verificar si la imagen está guardada en formato binario o base64
    if producto.imagen:
        # Si la imagen está en base64 (si es una cadena base64)
        if isinstance(producto.imagen, str):
            imagen_base64 = producto.imagen
        # Si la imagen está en binario (como bytes), convertirla a base64
        elif isinstance(producto.imagen, bytes):
            imagen_base64 = b64encode(producto.imagen).decode('utf-8')
    else:
        imagen_base64 = None


    # Verificar si el usuario está logueado
    nombre_usuario = None  # Variable para guardar el nombre del usuario logueado
    cedula = request.session.get('cedula')
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            nombre_usuario = usuario.nombre
        except Persona.DoesNotExist:
            pass

    return render(request, 'detalle_producto.html', {
        'producto': producto,
        'imagen_base64': imagen_base64,
        'logo': logo,
        'nombre_usuario': nombre_usuario,
    })
