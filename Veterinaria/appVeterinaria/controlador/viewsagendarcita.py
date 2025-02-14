from django.contrib import messages
from django.shortcuts import render, redirect
from base64 import b64encode
from django.db import transaction
from appVeterinaria.models import Persona, Mascota, Cita, ConfiguracionEmpresa


def agendar_cita(request):
    logo = None
    nombre_usuario = None  # Variable para guardar el nombre del usuario logueado
    configuracion = ConfiguracionEmpresa.objects.first()
    
    if configuracion and configuracion.logo:
        logo = f"data:image/png;base64,{b64encode(configuracion.logo).decode('utf-8')}"
        
    # Obtener el nombre del usuario autenticado
    usuario_autenticado = False
    cedula = request.session.get('cedula')
    
    if cedula:
        try:
            usuario = Persona.objects.get(cedula=cedula)
            usuario_autenticado = True
            nombre_usuario = usuario.nombre  # Extraemos el nombre del usuario logueado
        except Persona.DoesNotExist:
            usuario_autenticado = False    
    
    # Obtener los datos de la persona y su mascota si están registrados
    persona = None
    mascota = None
    cita = None

    if usuario_autenticado:
        persona = Persona.objects.filter(cedula=cedula).first()
        mascota = Mascota.objects.filter(cedula=persona).first() if persona else None
        cita = Cita.objects.filter(cedula=persona).first() if persona else None

    # Procesar el formulario al enviar los datos
    if request.method == 'POST':
        fecha = request.POST.get('appointmentDate')
        motivo = request.POST.get('reason')
        pet_id = request.POST.get('petid')
        pet_name = request.POST.get('petName')
        pet_age = request.POST.get('petAge', "Desconocida")
        pet_weight = request.POST.get('petWeight', 0.0)
        pet_size = request.POST.get('petSize', 0.0)
        pet_species = request.POST.get('petSpecies', "Desconocida")
        pet_color = request.POST.get('petColor', "Desconocido")
        phone_number = request.POST.get('phoneNumber')
        
        # Validar la cédula del dueño
        if not persona:
            messages.error(request, "No se encontró una persona asociada con esta cédula. Regístrese primero.")
            return redirect('register')
        
        # Guardar o actualizar la mascota
        mascota = Mascota.objects.filter(id_mascota=pet_id).first()
        if not mascota:
            # Crear una nueva mascota si no existe
            mascota = Mascota.objects.create(
                cedula=persona,
                nombre=pet_name,
                edad=pet_age,
                especie=pet_species,
                color=pet_color,
                tamaño=pet_size,
                peso=pet_weight
            )
        
        # Guardar la cita
        cita = Cita(
            fecha=fecha,
            motivo=motivo,
            cedula=persona,  # Instancia de Persona
            nroTel=phone_number,
            mascota=mascota  # Instancia de Mascota
        )


        try:
            # Guardar la instancia de la cita
            cita.save()
            messages.success(request, "Cita registrada exitosamente.")
            return redirect('agendar_cita')
        except Exception as e:
            messages.error(request, f"Error al registrar la cita: {str(e)}")
    
            
    # Si es un GET, renderizar el formulario con datos existentes
    context = {
        'persona': persona,
        'mascota': mascota,
        'cita': cita,
        'configuracion': configuracion,
        'logo': logo,
        'nombre_usuario': nombre_usuario,
        'usuario_autenticado': usuario_autenticado,
    }

    return render(request, 'agenda_cita.html', context)
    
