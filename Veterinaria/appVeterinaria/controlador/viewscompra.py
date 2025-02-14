import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from appVeterinaria.models import Tbproducto, ConfiguracionEmpresa, Persona, TbEncabFacVta, TbDetFactVta, Tbclientes
from django.utils.timezone import now
from base64 import b64encode

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def realizar_pago(request, producto_id):
    producto = get_object_or_404(Tbproducto, id=producto_id)

    # Obtener el logo desde ConfiguracionEmpresa
    logo = None
    configuracion = ConfiguracionEmpresa.objects.first()
    if configuracion and configuracion.logo:
        if isinstance(configuracion.logo, bytes):
            logo = f"data:image/png;base64,{b64encode(configuracion.logo).decode('utf-8')}"

    # Verificar si el usuario está logueado
    nombre_usuario = None
    cedula = request.session.get('cedula')
    cliente = None
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            nombre_usuario = usuario.nombre
            
            # Asociar cliente utilizando la cédula como identificador
            # Buscar o crear el cliente asociado en Tbclientes
            cliente, created = Tbclientes.objects.get_or_create(
                cedula=usuario,  # Relacionar con la cédula de la tabla Persona
                defaults={
                    'direccion': 'Sin dirección',
                    'nroTel': '0000000000',
                    'movil': '0000000000',
                    'email': usuario.email,
                }
            )
        except Persona.DoesNotExist:
            return render(request, 'error_pago.html', {'error': 'Usuario no encontrado'})
        
    factura = None  # Por defecto no hay factura para mostrar
    detalles_factura = []  # Detalles vacíos si no hay transacción

    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        token = request.POST.get('stripeToken')
        email = request.POST.get('email')  # Capturar el correo electrónico

        if token:
            total_venta = producto.vventa * cantidad

            try:
                # Crear el cliente en Stripe
                customer = stripe.Customer.create(
                    email=email,
                    source=token,  # Asociar el token del método de pago
                )

                # Crear el cargo con Stripe
                charge = stripe.Charge.create(
                    customer=customer.id,  # Usar el cliente creado
                    amount=int(total_venta * 100),  # Stripe maneja las cantidades en centavos
                    currency='usd',
                    description=f'Compra de {producto.nombre}',
                )

                # Reducir el stock
                producto.stock -= cantidad
                producto.save()
                
                
                # **Guardar en TbEncabFacVta**
                factura = TbEncabFacVta.objects.create(
                    nidCliente=cliente,
                    fechaVenta=now()
                )
                
                # **Guardar en TbDetFactVta**
                detalles_factura = TbDetFactVta.objects.create(
                    idFact=factura,
                    idProducto=producto,
                    val_venta=producto.vventa,
                    cant=cantidad
                )
                
                
                # Registrar la venta en la base de datos (opcional)
                # Aquí puedes agregar lógica para guardar la venta

                return redirect('compra_confirmada', producto_id=producto.id, cantidad=cantidad, total_venta=total_venta)

            except stripe.error.StripeError as e:
                return render(request, 'error_pago.html', {'error': str(e)})

    return render(request, 'formulario_pago.html', {
        'producto': producto,
        'logo': logo,
        'nombre_usuario': nombre_usuario,
        'factura': factura,
        'detalles_factura': detalles_factura,
    })
