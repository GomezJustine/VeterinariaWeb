from django.shortcuts import render, get_object_or_404
from appVeterinaria.models import Tbproducto, ConfiguracionEmpresa, Persona
from django.conf import settings
from base64 import b64encode

def formulario_pago(request, producto_id):
    producto = get_object_or_404(Tbproducto, id=producto_id)

    # Obtener el logo desde ConfiguracionEmpresa
    logo = None
    nombre_usuario = None  # Variable para guardar el nombre del usuario logueado
    configuracion = ConfiguracionEmpresa.objects.first()

    if configuracion:
        if configuracion.logo:
            logo = b64encode(configuracion.logo).decode('utf-8')


    # Verificar si el usuario está logueado
    cedula = request.session.get('cedula')
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            nombre_usuario = usuario.nombre  # Extraemos el nombre del usuario logueado
        except Persona.DoesNotExist:
            pass

    return render(request, 'formulario_pago.html', {
        'producto': producto,
        'STRIPE_TEST_PUBLIC_KEY': settings.STRIPE_TEST_PUBLIC_KEY,
        'logo': logo,
        'nombre_usuario': nombre_usuario,
    })

#codigo formulario pago