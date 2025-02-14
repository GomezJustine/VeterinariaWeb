from django.shortcuts import render, redirect
from appVeterinaria.models import Tbproducto, ConfiguracionEmpresa, Persona
from base64 import b64encode
from django.contrib import messages

def desactivar_producto(request):
    logo = None
    nombre_usuario = None  # Variable para guardar el nombre del usuario logueado


    # Obtener el logo desde ConfiguracionEmpresa
    configuracion = ConfiguracionEmpresa.objects.first()
    if configuracion and configuracion.logo:
        logo = f"data:image/png;base64,{b64encode(configuracion.logo).decode('utf-8')}"
    
    cedula = request.session.get('cedula')
    
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            nombre_usuario = usuario.nombre  # Extraemos el nombre del usuario logueado
        except Persona.DoesNotExist:
            pass

    if request.method == "POST":
        product_id = request.POST.get("productID")

        try:
            # Verificar si el producto existe
            producto = Tbproducto.objects.get(id=product_id)

            # Verificar si el producto ya está desactivado
            if not producto.activo:
                messages.warning(request, f"El producto con ID {product_id} ya está desactivado.")
            else:
                # Cambiar el estado activo a False
                producto.activo = False
                producto.save()
                messages.success(request, f"Producto con ID {product_id} desactivado correctamente.")

            return redirect('gestionproductos')  # Cambia al nombre de la URL de la gestión de productos

        except Tbproducto.DoesNotExist:
            messages.error(request, f"El producto con ID {product_id} no existe.")
            return redirect('desactivar_producto')  # Redirigir a la misma página

        except Exception as e:
            messages.error(request, f"Error al intentar desactivar el producto: {e}")
            return redirect('desactivar_producto')  # Redirigir a la misma página

    return render(request, "eliminar_producto.html", {
        "nombre_usuario": nombre_usuario,
        "logo": logo,
    })
