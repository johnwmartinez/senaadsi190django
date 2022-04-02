from django.contrib import admin

# Register your models here.
from .models import Producto
from .models import Marca
from .models import CategoriaProducto
from .models import Clientes
from .models import Orden_ventas

admin.site.register(Producto)
# admin.site.register(Marca)
admin.site.register(CategoriaProducto)
admin.site.register(Clientes)
admin.site.register(Orden_ventas)