from django.urls import path
from . import views
urlpatterns = [
    path('productos/', views.producto, name='producto'),
    path('productos/<int:id>', views.p_detalle, name='p_detalle'),
    path('carrito/', views.carrito, name='carrito'),
    path('realizar-pago/', views.realizar_pago, name='realizar_pago'),
]
