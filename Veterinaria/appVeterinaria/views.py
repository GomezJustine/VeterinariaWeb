from django.shortcuts import render
from django.shortcuts import render, redirect
import base64
from django.shortcuts import render
from models import ConfiguracionEmpresa

def inicio(request):
    # Recupera la configuración de la empresa (primera fila)
    config = ConfiguracionEmpresa.objects.first()
    
    # Convierte las imágenes a base64 si existen
    logo_base64 = base64.b64encode(config.logo).decode('utf-8') if config.logo else None
    logo1_base64 = base64.b64encode(config.logo1).decode('utf-8') if config.logo1 else None
    banner_base64 = base64.b64encode(config.banner).decode('utf-8') if config.banner else None

    context = {
        'nombre_empresa': config.nombre_empresa,
        'descripcion': config.descripcion,
        'direccion': config.direccion,
        'telefono': config.telefono,
        'email': config.email,
        'texto_footer': config.texto_footer,
        'logo_base64': logo_base64,
        'logo1_base64': logo1_base64,
        'banner_base64': banner_base64,
    }

    return render(request, 'iniciousuario.html', context)
def register_view(request):
    if request.method == 'POST':
        # Lógica para manejar el formulario de registro
        # Por ejemplo, crear un usuario o verificar los datos
        # Luego redirigir al inicio de sesión
        return redirect('login')  # Ajusta la URL del inicio de sesión según tu proyecto
    return render(request, 'register.html')  # Renderiza el template de registro

def crear_producto(request):
    # Implementación temporal o real de la vista
    return render(request, 'crear_producto.html')
# Implementación temporal o real de la vista

"""def crear_producto(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('productName')
        cantidad = request.POST.get('productQuantity')
        precio = request.POST.get('productPrice')

        # Validación y creación del producto
        if nombre and cantidad and precio:
            # Crear y guardar un nuevo producto en la base de datos
            nuevo_producto = Tbproducto(
                nombre=nombre,
                stock=cantidad,
                vventa=precio,
                vcompra=0,  # Puedes ajustar este valor según sea necesario
                descripcion="Nuevo producto"  # Puedes ajustar o hacer este campo opcional
            )
            nuevo_producto.save()
            # Mensaje de éxito
            messages.success(request, "Producto creado correctamente.")
            return redirect('crear_producto')  # Redirigir a la misma página para crear otro producto
        else:
            # Mensaje de error si faltan datos
            messages.error(request, "Por favor complete todos los campos.")
    
    # Si el método es GET, renderiza el formulario vacío
    return render(request, 'appVeterinaria/crear_producto.html')"""