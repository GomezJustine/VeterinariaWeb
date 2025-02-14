"""
URL configuration for Veterinaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from appVeterinaria.controlador.viewsautenticador import login_view
from appVeterinaria.controlador.viewsinicioadm import inicio_administrador
from appVeterinaria.controlador.viewsiniciousuario import inicio_usuario
from appVeterinaria.controlador.viewsregister import register_user
from appVeterinaria.controlador.viewsagregarproducto import crear_producto
from appVeterinaria.controlador.viewsmostrarlogo import mostrar_logo
from appVeterinaria.controlador.viewsgestioninventario import gestion_productos
from appVeterinaria.controlador.viewseditarproducto import editar_producto
from appVeterinaria.controlador.viewseliminarproducto import desactivar_producto
from appVeterinaria.controlador.viewscerrasesion import logout_view
from appVeterinaria.controlador.viewsinventario import inventario
from appVeterinaria.controlador.viewslistarproductos import listar_productos
from appVeterinaria.controlador.viewsperfil import perfil
from appVeterinaria.controlador.viewsajustes import configuracion_empresa
from appVeterinaria.controlador.viewsagendarcita import agendar_cita
from appVeterinaria.controlador.viewsconsultascitas import consultas_citas
from appVeterinaria.controlador.viewsconsultascitas import cambiar_estado_cita
from appVeterinaria.controlador.viewsproductos  import listar_productos_cliente 
from appVeterinaria.controlador.viewsdetallesproductos import detalle_producto
from appVeterinaria.controlador.viewsdetallesproductos import detalle_producto 
from appVeterinaria.controlador.viewsformulariopago import formulario_pago
from appVeterinaria.controlador.viewscompra import realizar_pago
from appVeterinaria.controlador.viewscompraconfirmada import compra_confirmada
urlpatterns = [
    path('', inicio_usuario, name='iniciousuario'),  # Ruta vacía para la página principal
    path('Inicio/', inicio_usuario, name='home'),  # También mantienes la ruta 'Inicio/'
    path('login/', login_view, name='login'),
    path('iniciousuario/', inicio_usuario, name='iniciousuario'),  # Vista para usuarios
    path('inicioadm/', inicio_administrador, name='inicioadm'),  # Vista para administradores
    path('register/', register_user, name='register'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('mostrar_logo/', mostrar_logo, name='mostrar_logo'),
    path('gestionproductos/', gestion_productos, name='gestionproductos'),
    path('inventario/', inventario, name='inventario'),
    path('editar_producto/', editar_producto, name='editar_producto'),
    path('desactivar_producto/', desactivar_producto, name='desactivar_producto'),  # Nueva ruta
    path('listar_productos/', listar_productos, name='listar_productos'),
    path('logout/', logout_view, name='logout'),  # Ruta para cerrar sesión
    path('perfil/', perfil, name='perfil'),
    path('ajustes/', configuracion_empresa, name='ajustes'),
    path('agendar_cita/', agendar_cita, name='agendar_cita'),
    path('consultas/', consultas_citas, name='consultas'),
    path('cambiar_estado_cita/<int:id_cita>/', cambiar_estado_cita, name='cambiar_estado_cita'),
    path('productos/', listar_productos_cliente, name='listar_productos_cliente'), #productostienda
    path('producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('producto/<int:producto_id>/pago/', formulario_pago, name='formulario_pago'),
    path('producto/<int:producto_id>/realizar_pago/', realizar_pago, name='realizar_pago'),
    path('compra_confirmada/<int:producto_id>/<int:cantidad>/<int:total_venta>/', compra_confirmada, name='compra_confirmada'),
]


