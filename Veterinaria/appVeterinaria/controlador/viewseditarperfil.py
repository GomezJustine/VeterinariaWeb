from django.shortcuts import render, redirect
from appVeterinaria.models import Persona

def editar_perfil(request):
    # Obtener el usuario autenticado mediante la sesión
    cedula = request.session.get('cedula')
    if not cedula:
        return redirect('login')  # Redirigir al login si no está autenticado

    try:
        usuario = Persona.objects.get(cedula=cedula)
    except Persona.DoesNotExist:
        return redirect('perfil')  # Redirigir al perfil si no se encuentra al usuario

    if request.method == "POST":
        # Actualizar los datos del usuario
        usuario.nombre = request.POST.get('nombre', usuario.nombre)
        usuario.apellido = request.POST.get('apellido', usuario.apellido)
        usuario.edad = request.POST.get('edad', usuario.edad)
        usuario.email = request.POST.get('email', usuario.email)
        usuario.telefono = request.POST.get('telefono', usuario.telefono)
        usuario.save()
        return redirect('perfil')  # Redirigir al perfil después de guardar

    return render(request, 'editar_perfil.html', {"usuario": usuario})
