from django.db import models

# Clase Marcas (se relaciona a productos)


class Marca(models.Model):
    marca = models.CharField(max_length=200)
    #
    """
    # Esta clase Meta se usa para reconfigurar parámetros por defecto
    class Meta:
       db_table = "marcas" # Esto es si la tabla se llama marcas
       verbose_name = "marca" # Nombre en singular
       verbose_name_plural = "marcas" # Nombre en plural
    """

    def __str__(self):
        return self.marca

# Clase Categoría de producto


class CategoriaProducto(models.Model):
    categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.categoria

# Clase Producto


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    sku = models.CharField(max_length=150, unique=True, null=True)
    descripcion = models.TextField(null=True, blank=True)
    cantidad = models.PositiveBigIntegerField()
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='static/img/productos/')
    id_categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE, default=1)

    class Estado(models.IntegerChoices):
        Activo = 1
        Inactivo = 0
    estado = models.IntegerField(choices=Estado.choices, default=1)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    session = models.TextField(null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)
    precio = models.FloatField(default=1.0, blank=True, null=True)
    cantidad = models.PositiveBigIntegerField()
    
class Clientes(models.Model):
    nombre = models.TextField()
    apellido = models.TextField()
    cedula = models.TextField(null=True, blank=True)
    pais = models.TextField()
    direccion = models.TextField()
    direccion_aux = models.TextField(null=True, blank=True)
    departamento = models.TextField()
    ciudad = models.TextField()
    codigo_postal = models.TextField(null=True, blank=True)
    telefono = models.TextField()
    email = models.TextField()
    def __str__(self):
        return self.nombre
    
class Orden_ventas(models.Model):
    ESTADOS = (
        ('Pendiente', 'Pendiente'),
        ('Pago en proceso', 'Pago en proceso'),
        ('Pago aceptado', 'Pago aceptado'),
        ('En trámite', 'En trámite'),
        ('Despachado', 'Despachado'),
    )
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, default=1)
    total = models.TextField()
    session_id = models.TextField(editable=False)
    estado = models.CharField(max_length=200, null=True, choices=ESTADOS)
    def __str__(self):
        return self.cliente.nombre + ' ' + self.cliente.apellido + ' - ' + self.cliente.email

class Orden_productos(models.Model):
    orden = models.ForeignKey(Orden_ventas, on_delete=models.CASCADE, default=1)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)
    precio = models.TextField()
    cantidad = models.TextField()
    subtotal = models.TextField()
    
    

    
    
