from django.shortcuts import render, get_object_or_404, redirect
from appVeterinaria.models import ConfiguracionEmpresa, Cita, Persona, Mascota
from base64 import b64encode
from appVeterinaria.models import Cita

def consultas_citas(request):
    logo = None
    nombre_usuario = None  # Variable para guardar el nombre del usuario logueado

    # Obtener logo desde ConfiguracionEmpresa
    configuracion = ConfiguracionEmpresa.objects.first()
    if configuracion and configuracion.logo:
        # Verificar que el logo sea de tipo bytes antes de codificarlo
        if isinstance(configuracion.logo, bytes):
            logo = f"data:image/png;base64,{b64encode(configuracion.logo).decode('utf-8')}"
        else:
            logo = None  # Manejar casos donde no es válido

    # Verificar si el usuario está logueado
    cedula = request.session.get('cedula')
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            nombre_usuario = usuario.nombre
        except Persona.DoesNotExist:
            pass

    # Consultar citas
    citas_pendientes = Cita.objects.filter(estado=True).select_related('cedula', 'mascota')
    citas_atendidas = Cita.objects.filter(estado=False).select_related('cedula', 'mascota')

    return render(request, 'consultas.html', {
        'citas_pendientes': citas_pendientes,
        'citas_atendidas': citas_atendidas,
        'logo': logo,
        'nombre_usuario': nombre_usuario,
    })

def cambiar_estado_cita(request, id_cita):
    # Obtener la cita o devolver un error 404 si no existe
    cita = get_object_or_404(Cita, id_cita=id_cita)

    # Cambiar el estado de la cita a False (Atendida)
    cita.estado = False
    cita.save()

    # Redirigir de vuelta a la página de consultas
    return redirect('consultas')