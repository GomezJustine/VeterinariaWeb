#Base de datos
from django.db import models

# Modelo que representa a una persona (autenticación y roles)
class Persona(models.Model):
    cedula = models.PositiveIntegerField(primary_key=True)  # Identificador único
    nombre = models.CharField(max_length=50)  # Nombre completo
    email = models.EmailField(max_length=100, unique=True, default='example@example.com')  # Email único con valor por defecto
    contraseña = models.CharField(max_length=255, default='123')  # Contraseña encriptada con valor por defecto
    rol = models.CharField(
        max_length=20,
        choices=[('cliente', 'Cliente'), ('administrador', 'Administrador')],
        default='cliente'  # Valor por defecto para el rol
    )  # Rol del usuario

    class Meta:
        db_table = 'persona'



# Modelo para representar los datos de clientes
class Tbclientes(models.Model):
    nidCliente = models.AutoField(primary_key=True)  # Cambiado a coincidir con la base de datos
    direccion = models.CharField(max_length=100, default="Sin dirección")
    nroTel = models.CharField(max_length=20, default="0000000000")  # Cambiado a camelCase
    movil = models.CharField(max_length=20, default="0000000000")   # Sin cambios
    email = models.EmailField(max_length=50, default="email@ejemplo.com")
    cedula = models.ForeignKey('Persona', on_delete=models.SET_NULL, blank=True, null=True, db_column='cedula')

    class Meta:
        db_table = 'tbclientes'  # Asegúrate de que coincide con el nombre de la tabla SQL


# Modelo para representar las categorías de productos
class Tbcategorias(models.Model):
    idCategoria = models.AutoField(primary_key=True)  # Nombre alineado con la base de datos
    descripcion = models.CharField(max_length=60, default="Sin descripción")

    class Meta:
        db_table = 'tbcategorias'


# Modelo para representar los productos de la tienda
class Tbproducto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, default="Producto sin nombre")
    descripcion = models.CharField(max_length=100, default="Sin descripción")
    vcompra = models.IntegerField(default=0)
    vventa = models.IntegerField(default=0)
    stock = models.FloatField(default=0.0)
    idCategoria = models.ForeignKey(Tbcategorias, on_delete=models.CASCADE, db_column='idCategoria')
    imagen = models.BinaryField(null=True, blank=True)
    activo = models.BooleanField(default=True)  # Campo para activar/desactivar productos

    class Meta:
        db_table = 'tbproducto'


# Modelo para representar proveedores
class TbProveedor(models.Model):
    nid_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, default="Sin nombre")
    descripcion = models.CharField(max_length=100, default="Sin descripción")
    direccion = models.CharField(max_length=100, default="Sin dirección")
    nro_tel = models.CharField(max_length=20, default="0000000000")
    email = models.EmailField(max_length=50, default="email@ejemplo.com")

    class Meta:
        db_table = 'tbProveedor'

# Modelo para el encabezado de compras
class TbcomprasEncab(models.Model):
    id_compra = models.AutoField(primary_key=True)
    nid_proveedor = models.ForeignKey(TbProveedor, on_delete=models.CASCADE)
    fecha_compra = models.DateField(blank=True, null=True, default="2000-01-01")

    class Meta:
        db_table = 'tbcomprasEncab'

# Modelo para el detalle de las compras
class TbComprasDetalle(models.Model):
    id_compra = models.ForeignKey(TbcomprasEncab, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Tbproducto, on_delete=models.CASCADE)
    val_compra = models.FloatField(default=0.0)
    cant = models.IntegerField(default=1)

    class Meta:
        db_table = 'tbComprasDetalle'
        unique_together = (('id_compra', 'id_producto'),)

# Modelo para el encabezado de ventas
class TbEncabFacVta(models.Model):
    idFact = models.AutoField(primary_key=True)
    nidCliente = models.ForeignKey(Tbclientes, on_delete=models.CASCADE, db_column='nidCliente')
    fechaVenta = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'tbEncabFacVta'

# Modelo para el detalle de la factura de venta
class TbDetFactVta(models.Model):
    idFact = models.ForeignKey(TbEncabFacVta, on_delete=models.CASCADE, db_column='idFact', primary_key=True)  # Clave primaria
    idProducto = models.ForeignKey(Tbproducto, on_delete=models.CASCADE, db_column='idProducto')
    val_venta = models.FloatField(default=0.0)  # Cambia 0.0 por el valor que tenga sentido
    cant = models.IntegerField()

    class Meta:
        db_table = 'tbDetFactVta'
        unique_together = (('idFact', 'idProducto'),)

# Modelo para registrar mascotas
class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    cedula = models.ForeignKey('Persona', on_delete=models.CASCADE, db_column='cedula')
    nombre = models.CharField(max_length=50, default="Sin nombre")  # Nuevo campo
    edad = models.CharField(max_length=50, blank=True, null=True, default="Desconocida")
    especie = models.CharField(max_length=40, blank=True, null=True, default="Desconocida")
    color = models.CharField(max_length=40, blank=True, null=True, default="Desconocido")
    tamaño = models.FloatField(default=0.0)
    peso = models.FloatField(default=0.0)

    class Meta:
        db_table = 'mascota'

# Modelo para registrar historias clínicas de mascotas
class HistoriaClinica(models.Model):
    id = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey('Persona', on_delete=models.SET_NULL, blank=True, null=True)
    id_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    motivo_consulta = models.CharField(max_length=200, default="Sin motivo")
    sistematologia = models.CharField(max_length=100, default="Sin datos")
    diagnostico = models.CharField(max_length=200, default="Sin diagnóstico")
    procedimiento = models.CharField(max_length=500, default="Sin procedimiento")
    medicamento = models.CharField(max_length=30, default="Sin medicamento")
    dosis = models.CharField(max_length=40, default="Sin dosis")

    class Meta:
        db_table = 'historia_clinica'

# Modelo para roles adicionales o cargos en el sistema
class Cargo(models.Model):
    idcargo = models.AutoField(primary_key=True)
    descripcion_cargo = models.CharField(max_length=60, default="Sin descripción")

    class Meta:
        db_table = 'cargo'

# Modelo para alertas de stock bajo en productos
class TbAlertaStock(models.Model):
    id_alerta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Tbproducto, on_delete=models.CASCADE)
    fecha_alerta = models.DateField(blank=True, null=True, default="2000-01-01")
    stock_actual = models.FloatField(default=0.0)

    class Meta:
        db_table = 'tbAlertaStock'

# Modelo para registrar órdenes de compra
class OrdenCompra(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_compra = models.ForeignKey(TbcomprasEncab, on_delete=models.SET_NULL, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True, default="Pendiente")
    fecha_orden = models.DateField(blank=True, null=True, default="2000-01-01")

    class Meta:
        db_table = 'OrdenCompra'

# Modelo para gestionar el carrito de compras de clientes
class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    nid_cliente = models.ForeignKey(Tbclientes, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(blank=True, null=True, default="2024-11-29")

    class Meta:
        db_table = 'Carrito'

# Modelo para el detalle del carrito de compras
class DetalleCarrito(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Tbproducto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    class Meta:
        db_table = 'DetalleCarrito'

# Modelo para el registro de pagos asociados a ventas
class Pagos(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_fact = models.ForeignKey(TbEncabFacVta, on_delete=models.SET_NULL, blank=True, null=True, db_column='idFact')
    metodo_pago = models.CharField(max_length=30, blank=True, null=True, default="Efectivo")
    monto = models.FloatField(default=0.0)
    fecha_pago = models.DateField(blank=True, null=True, default="2000-01-01")

    class Meta:
        db_table = 'Pagos'


# Modelo para la configuración de la empresa
class ConfiguracionEmpresa(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    texto_footer = models.TextField(null=True, blank=True)
    logo = models.BinaryField(null=True, blank=True)
    logo1 = models.BinaryField(null=True, blank=True)
    banner = models.BinaryField(null=True, blank=True)
    banner1 = models.BinaryField(null=True, blank=True)
    banner2 = models.BinaryField(null=True, blank=True)
    banner3 = models.BinaryField(null=True, blank=True)
    banner4 = models.BinaryField(null=True, blank=True)
    banner5 = models.BinaryField(null=True, blank=True)
    
    class Meta:
        db_table = 'Configuracionempresa'

# Modelo para representar las citas
class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    fecha = models.DateField(null=False)  # No permitir valores nulos
    motivo = models.TextField(null=False)  # Motivo debe ser obligatorio
    cedula = models.ForeignKey(Persona, on_delete=models.CASCADE)  # Relación obligatoria
    nroTel = models.CharField(max_length=20, null=False)  # Obligatorio
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='id_mascota'  # Indica el nombre exacto de la columna en la base de datos
    )
    estado = models.BooleanField(default=True)  # True: Pendiente, False: Atendida
    class Meta:
        db_table = 'cita'
