from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.db import models

# Create your views here.
from .models import Producto, CategoriaProducto, Carrito, Orden_ventas, Clientes, Orden_productos
from .forms import Orden_ventasForm



def producto(request):
    request.session['inicial'] = 1
    productos = Producto.objects.all()
    categorias = CategoriaProducto.objects.exclude(pk = 1)
    return render(request, 'producto/index.html', {
        'categorias':categorias,
        'productos': productos,
        'todos_los_productos':len(productos),
        'correo': 'info@softbox190.com',
        'celular': '+57 300 423 5239',
        'direccion': 'Carrera 12 #34-56',
        'promesa': 'Compra y paga contraentrega',
        'social_media' : [
            {
                'enlace':'#',
                'class':'fa fa-facebook',
            },
            {
                'enlace':'#',
                'class':'fa fa-twitter',
            },
            {
                'enlace':'#',
                'class':'fa fa-linkedin',
            },
            {
                'enlace':'#',
                'class':'fa fa-pinterest-p',
            },
        ],
        'logo':{
            'url':'#',
            'src':'/static/img/logo.png',
        },
        'menu_ppal':[
            {
                'url':'#',
                'label':'Inicio',
                'class':'active',
            },
            {
                'url':'#',
                'label':'Quienes Somos',
            },
            {
                'url':'#',
                'label':'Tienda',
            },
            {
                'url':'#',
                'label':'Contáctenos',
            },
        ],
        'carrito':{
            'total':'$150.000',
            'cant':3,
        },
        'hero':{
            'subtitulo':'Más reciente',
            'h21':'CPU Game Max',
            'h22':'para gamers pro',
            'p':'100% personalizado, en AMD o Intel',
            'boton':'ÁRMALO AHORA',
            'boton_url':'#',
        },
        'owl_categorias':[
            {
                'url':'#',
                'label':'Audifonos',
                'imagen':'/static/img/categorias/headphones.jpg',
            },
            {
                'url':'#',
                'label':'Teclados',
                'imagen':'/static/img/categorias/keyboard.jpg',
            },
            {
                'url':'#',
                'label':'Portátiles',
                'imagen':'/static/img/categorias/laptops.jpg',
            },
            {
                'url':'#',
                'label':'Monitores',
                'imagen':'/static/img/categorias/monitor.jpg',
            },
            {
                'url':'#',
                'label':'Mouses',
                'imagen':'/static/img/categorias/mouse.jpg',
            },
        ]
    })
    
def categoriaProducto(request):
    request.session['inicial'] = 1
    categoria = CategoriaProducto.objects.all()
    return render(request, 'producto/index.html', {
        'categoria': categoria
    })
    
def p_detalle(request, id):
    request.session['inicial'] = 1
    producto = get_object_or_404(Producto, pk=id)
    random = Producto.objects.order_by('?')[:4]
    # return HttpResponse("oksss")
    return render(request, 'producto/individual.html', {
        'producto': producto,
        'randoms':random,
    })

def carrito(request):
    request.session['inicial'] = 1
    carrito = Carrito.objects.filter(session=request.session.session_key)
    productos = Producto.objects.all()
    cart_total = 0
    # productos = models.ForeignKey(Producto)
    for carrito_indv in carrito:
        cart_total += carrito_indv.precio * carrito_indv.cantidad 
    return render(request, 'producto/carrito.html', {
        'carritos':carrito,
        'cantidad_productos':len(carrito),
        'productos':productos,
        'valor_sumatoria': cart_total
    })


def realizar_pago(request):
    request.session['inicial'] = 1
    carrito = Carrito.objects.filter(session=request.session.session_key)
    productos = Producto.objects.all()
    # Total productos
    cart_total = 0
    for carrito_indv in carrito:
        cart_total += carrito_indv.precio * carrito_indv.cantidad 
        
    form = Orden_ventasForm()
    
    if request.method == 'POST':

        form = Orden_ventasForm(request.POST)
        # Guardamos la información en DB
        ventas = Orden_ventas.objects.all()
        cliente = Clientes.objects.all()
        ventas_productos = Orden_productos.objects.all()
        # Creamos el cliente
        '''
        '''
        cliente_nuevo = cliente.create(
            nombre=request.POST['nombre'], 
            apellido = request.POST['apellido'],
            pais = request.POST['pais'],
            direccion = request.POST['direccion'],
            departamento = request.POST['direccion_aux'],
            ciudad = request.POST['ciudad'],
            codigo_postal = request.POST['codigo_postal'],
            telefono = request.POST['telefono'],
            email = request.POST['email'],
        )
        # Creamos la venta
        venta_nueva = ventas.create(session_id=request.session.session_key, total=request.POST['venta_total'], cliente=Clientes.objects.get(id=cliente_nuevo.id), estado='Pendiente')
        
        #Creamos los productos asociados de la venta
        productos_de_venta = Carrito.objects.filter(session=request.session.session_key)
        for cada_venta in productos_de_venta:
            # print(cada_venta.precio)
            ventas_productos.create(
                orden_id = venta_nueva.id,
                producto_id = cada_venta.producto_id,
                precio = cada_venta.precio,
                cantidad = cada_venta.cantidad,
                subtotal = cada_venta.cantidad * cada_venta.precio,
            )
        
        # Eliminamos el carrito de session
        del request.session['cartdata']
        # Eliminamos el carrito de DB
        Carrito.objects.filter(session=request.session.session_key).delete()
        # Redireccionamos a la página de gracias
        return redirect('/gracias')
            
        
    return render(request, 'producto/checkout.html', {
        'carritos':carrito,
        'cantidad_productos':len(carrito),
        'productos':productos,
        'valor_sumatoria': cart_total,
        'form':form,
    })

####