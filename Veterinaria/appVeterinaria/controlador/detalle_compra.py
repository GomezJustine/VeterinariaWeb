import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from appVeterinaria.models import Tbproducto

# Configurar Stripe con tu clave secreta
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def detalle_compra(request, producto_id):
    # Obtener el producto
    producto = get_object_or_404(Tbproducto, id=producto_id)

    # Si el formulario fue enviado
    if request.method == 'POST':
        # Obtener la cantidad y token del formulario
        cantidad = int(request.POST.get('cantidad', 1))
        token = request.POST.get('stripeToken')

        if token:
            total_venta = producto.vventa * cantidad  # Calcular el total

            try:
                # Crear el cargo con Stripe
                charge = stripe.Charge.create(
                    amount=int(total_venta * 100),  # Stripe trabaja con centavos
                    currency='usd',
                    description=f'Compra de {producto.nombre}',
                    source=token  # Usamos el token generado en el frontend
                )

                # Aquí puedes agregar lógica para registrar la compra en la base de datos

                # Redirigir a la página de compra confirmada
                return redirect('compra_confirmada', producto_id=producto.id, cantidad=cantidad, total_venta=total_venta)

            except stripe.error.StripeError as e:
                # Si hay un error con el pago, mostrar el error
                return render(request, 'error_pago.html', {'error': str(e)})

    return render(request, 'detalle_compra.html', {'producto': producto})
