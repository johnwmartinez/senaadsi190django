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

# Clase Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    cantidad = models.PositiveBigIntegerField()
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='static/img/productos/')
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre