from django.forms import ModelForm
from .models import Orden_ventas, Orden_productos

class Orden_ventasForm(ModelForm):
    class Meta:
        model = Orden_ventas
        fields = '__all__'