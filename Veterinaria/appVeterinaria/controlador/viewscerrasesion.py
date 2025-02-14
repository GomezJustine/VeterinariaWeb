from django.shortcuts import redirect

def logout_view(request):
    request.session.flush()  # Limpiar todos los datos de la sesión
    return redirect('login')  # Redirigir al login
