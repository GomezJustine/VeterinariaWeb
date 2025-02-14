from django.http import HttpResponse
from appVeterinaria.models import ConfiguracionEmpresa

def mostrar_logo(request):
    try:
        configuracion = ConfiguracionEmpresa.objects.get(nombre_empresa="Centro Veterinario JSJB")
        response = HttpResponse(configuracion.logo, content_type="image/png")
        return response
    except ConfiguracionEmpresa.DoesNotExist:
        return HttpResponse("No hay logo disponible", content_type="text/plain")
