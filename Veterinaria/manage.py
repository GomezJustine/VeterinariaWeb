#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import webbrowser #para abrir la pagina princpial al correr el servidor

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Veterinaria.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    
    # Ejecutar el servidor y abrir el navegador automáticamente si es 'runserver'
    if len(sys.argv) > 1 and sys.argv[1] == "runserver":
        PORT = os.getenv('PORT', '8000')  # Obtener el puerto configurado o el predeterminado
        URL = f"http://127.0.0.1:{PORT}/"  # URL del servidor
        webbrowser.open(URL)  # Abrir el navegador
    
    execute_from_command_line(sys.argv)  # Ejecutar comando de línea de Django
    
if __name__ == '__main__':
    main()
