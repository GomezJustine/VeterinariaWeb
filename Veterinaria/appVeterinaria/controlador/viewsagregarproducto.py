from django.shortcuts import render, redirect
from django.core.files.uploadedfile import InMemoryUploadedFile
from appVeterinaria.models import ConfiguracionEmpresa, Tbproducto, Tbcategorias, Persona
from base64 import b64encode
from decimal import Decimal #

def crear_producto(request):
    logo = None
    nombre_usuario = None  # Variable para guardar el nombre del usuario logueado

    # Obtener logo desde ConfiguracionEmpresa
    configuracion = ConfiguracionEmpresa.objects.first()
    if configuracion and configuracion.logo:
        logo = f"data:image/png;base64,{b64encode(configuracion.logo).decode('utf-8')}"

    if request.method == "POST":
        # Obtener los datos del formulario
        product_name = request.POST.get("productName")
        product_quantity = request.POST.get("productQuantity")
        product_price = request.POST.get("productPrice").replace(".", "")  # Eliminar separadores de miles
        product_image = request.FILES.get("productImage")
        category_id = request.POST.get("productCategory")  # ID de categoría enviado desde el formulario
        product_description = request.POST.get("productDescription", "Sin descripción")  # Capturar descripción

        # Validaciones básicas
        if not all([product_name, product_quantity, product_price, category_id]):
            return render(request, "agregarproducto.html", {
                "logo": logo,
                "error": "Todos los campos son obligatorios.",
            })

        try:
            # Validar que el precio sea un número válido
            try:
                product_price = Decimal(product_price)  # Convertir a decimal
            except Exception:
                return render(request, "agregarproducto.html", {
                    "logo": logo,
                    "error": "El precio debe ser un número válido (sin puntos ni caracteres especiales).",
                })

            # Verificar que la categoría seleccionada existe
            categoria = Tbcategorias.objects.get(idCategoria=category_id)

            # Crear y guardar el producto
            producto = Tbproducto(
                nombre=product_name,
                descripcion=product_description,  # Guardar la descripción capturada
                vcompra=0,  # Valor predeterminado
                vventa=product_price,
                stock=product_quantity,
                idCategoria=categoria,
                imagen=product_image.read() if isinstance(product_image, InMemoryUploadedFile) else None,
            )
            producto.save()

            # Redirigir a la página de gestión de productos
            return redirect("gestionproductos")

        except Tbcategorias.DoesNotExist:
            return render(request, "agregarproducto.html", {
                "logo": logo,
                "error": "La categoría seleccionada no existe.",
            })
        except Exception as e:
            return render(request, "agregarproducto.html", {
                "logo": logo,
                "error": f"Error al guardar el producto: {e}",
            })

    cedula = request.session.get('cedula')
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            nombre_usuario = usuario.nombre  # Extraemos el nombre del usuario logueado
        except Persona.DoesNotExist:
            pass

    # Renderizar el formulario con categorías disponibles
    categorias = Tbcategorias.objects.all()
    return render(request, "agregarproducto.html", {
        "logo": logo,
        "categorias": categorias,
        "nombre_usuario": nombre_usuario,  # Pasar el nombre del usuario al template
    })
