from django.shortcuts import render, get_object_or_404
from appVeterinaria.models import Tbproducto, TbEncabFacVta, TbDetFactVta, ConfiguracionEmpresa, Persona
from base64 import b64encode

def compra_confirmada(request, producto_id, cantidad, total_venta):
    # Obtener el producto
    producto = get_object_or_404(Tbproducto, id=producto_id)

    # Obtener el logo desde ConfiguracionEmpresa
    logo = None
    configuracion = ConfiguracionEmpresa.objects.first()
    if configuracion and configuracion.logo:
        logo = f"data:image/png;base64,{b64encode(configuracion.logo).decode('utf-8')}"

    # Verificar si el usuario está logueado
    nombre_usuario = None
    cedula = request.session.get('cedula')
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            nombre_usuario = usuario.nombre
        except Persona.DoesNotExist:
            pass

    # Si deseas agregar información adicional desde las tablas de facturación:
    factura = TbEncabFacVta.objects.filter(nidCliente__cedula=cedula).last() if cedula else None
    detalles_factura = TbDetFactVta.objects.filter(idFact=factura) if factura else []

    # Renderizar la página de confirmación de compra
    return render(request, 'compra_confirmada.html', {
        'producto': producto,
        'cantidad': cantidad,
        'total_venta': total_venta,
        'factura': factura,
        'detalles_factura': detalles_factura,
        'logo': logo,
        'nombre_usuario': nombre_usuario,
    })


