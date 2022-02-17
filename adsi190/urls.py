from django.contrib import admin
from django.urls import path, include
import tienda
from tienda.models import Producto
from .import views

urlpatterns = [
    path('login/',views.login, name='login'),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('quienes-somos/', views.quienes_somos, name="quienes_somos"),
    path('', views.home, name='producto'),
    path('', include('tienda.urls')),
   
]