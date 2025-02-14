from django.shortcuts import render, get_object_or_404
from appVeterinaria.models import Tbproducto, Tbcategorias, ConfiguracionEmpresa, Persona
from base64 import b64encode


def editar_producto(request):
    logo = None
    nombre_usuario = None  # Variable para guardar el nombre del usuario logueado

    # Obtener logo desde ConfiguracionEmpresa
    configuracion = ConfiguracionEmpresa.objects.first()
    if configuracion and configuracion.logo:
        logo = f"data:image/png;base64,{b64encode(configuracion.logo).decode('utf-8')}"

    # Obtener el nombre del usuario autenticado
    cedula = request.session.get('cedula')
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            nombre_usuario = usuario.nombre  # Extraemos el nombre del usuario logueado
        except Persona.DoesNotExist:
            pass

    producto = None  # Para almacenar el producto cargado (si se encuentra)
    categorias = Tbcategorias.objects.all()  # Obtener todas las categorías disponibles

    if request.method == "POST":
        if "buscarProducto" in request.POST:  # Verificar si es búsqueda
            product_id = request.POST.get("productID")
            if not product_id:
                return render(request, "editarproducto.html", {
                    "logo": logo,
                    "error": "Por favor, ingrese un ID de producto válido.",
                    "categorias": categorias,
                    "nombre_usuario": nombre_usuario,
                })

            # Intentar cargar el producto
            try:
                producto = Tbproducto.objects.get(id=product_id)
            except Tbproducto.DoesNotExist:
                return render(request, "editarproducto.html", {
                    "logo": logo,
                    "error": "El producto con el ID proporcionado no existe.",
                    "categorias": categorias,
                    "nombre_usuario": nombre_usuario,
                })

            return render(request, "editarproducto.html", {
                "logo": logo,
                "producto": producto,
                "categorias": categorias,
                "nombre_usuario": nombre_usuario,
            })

        # Si no es búsqueda, es edición
        product_id = request.POST.get("productID")
        try:
            producto = Tbproducto.objects.get(id=product_id)
        except Tbproducto.DoesNotExist:
            return render(request, "editarproducto.html", {
                "logo": logo,
                "error": "El producto con el ID proporcionado no existe.",
                "categorias": categorias,
                "nombre_usuario": nombre_usuario,
            })

        # Si los campos están vacíos, no se actualizan
        product_name = request.POST.get("productName")
        product_quantity = request.POST.get("productQuantity")
        product_price = request.POST.get("productPrice")
        product_image = request.FILES.get("productImage")
        product_category = request.POST.get("productCategory")
        product_description = request.POST.get("productDescription")  # Capturar la descripción

        # Actualizar solo los campos modificados
        if product_name:
            producto.nombre = product_name
        if product_quantity:
            try:
                quantity = int(product_quantity)
                if quantity < 0:
                    raise ValueError("No se permiten valores negativos para el stock.")
                producto.stock += quantity
            except ValueError as e:
                return render(request, "editarproducto.html", {
                    "logo": logo,
                    "error": str(e),
                    "producto": producto,
                    "categorias": categorias,
                    "nombre_usuario": nombre_usuario,
                })
        if product_price:
            try:
                nuevo_precio = int(product_price)
                if nuevo_precio <= 0:
                    raise ValueError("El precio debe ser mayor a 0.")
                producto.vventa = nuevo_precio
            except ValueError as e:
                return render(request, "editarproducto.html", {
                    "logo": logo,
                    "error": str(e),
                    "producto": producto,
                    "categorias": categorias,
                    "nombre_usuario": nombre_usuario,
                })
        if product_category:
            try:
                categoria = Tbcategorias.objects.get(idCategoria=product_category)
                producto.idCategoria = categoria
            except Tbcategorias.DoesNotExist:
                return render(request, "editarproducto.html", {
                    "logo": logo,
                    "error": "La categoría seleccionada no existe.",
                    "producto": producto,
                    "categorias": categorias,
                    "nombre_usuario": nombre_usuario,
                })
        if product_image:
            producto.imagen = product_image.read()
        if product_description:  # Verificar si hay una descripción proporcionada
            producto.descripcion = product_description

        # Guardar cambios en la base de datos
        producto.save()

        return render(request, "editarproducto.html", {
            "logo": logo,
            "success": "Producto actualizado correctamente.",
            "producto": producto,
            "categorias": categorias,
            "nombre_usuario": nombre_usuario,
        })

    # Renderizar la página vacía o con datos
    return render(request, "editarproducto.html", {
        "logo": logo,
        "producto": producto,
        "categorias": categorias,
        "nombre_usuario": nombre_usuario,
    })
