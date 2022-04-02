from tokenize import Double
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from django.contrib.auth import login as lg
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from tienda.views import Producto, CategoriaProducto, Carrito

from django.utils.datastructures import MultiValueDictKeyError

from decimal import Decimal

def saludo(request):
    request.session['inicial'].update(1)
    productos = Producto.objects.all()
    # CategoriaProducto = CategoriaProducto.objects.all()
    return render(request, 'index.html', {
        'correo': 'info@softbox190.com_',
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
            'src':'static/img/logo.png',
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
        'categorias':[
            {
            'label' : 'Monitores', 
            'url' : '#',
            },
            {
            'label': 'Teclados y Mouses',  
            'url' : '#',
            },
            {
            'label': 'Tarjetas de Video', 
            'url' : '#',
            },
            {
            'label': 'RAM', 
            'url' : '#',
            },
            {
            'label': 'Discos SSD', 
            'url' : '#',
            },
            {
            'label': 'Portátiles', 
            'url' : '#',
            },
            {
            'label': 'Celulares', 
            'url' : '#',
            },
            {
            'label': 'Tablets', 
            'url' : '#',
            },
            {
            'label': 'Consolas', 
            'url' : '#',
            },
            {
            'label': 'Aplicaciones', 
            'url' : '#',
            },
            {
            'label': 'Sitios Web',
            'url' : '#',
            },
        ],
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
                'imagen':'static/img/categorias/headphones.jpg',
            },
            {
                'url':'#',
                'label':'Teclados',
                'imagen':'static/img/categorias/keyboard.jpg',
            },
            {
                'url':'#',
                'label':'Portátiles',
                'imagen':'static/img/categorias/laptops.jpg',
            },
            {
                'url':'#',
                'label':'Monitores',
                'imagen':'static/img/categorias/monitor.jpg',
            },
            {
                'url':'#',
                'label':'Mouses',
                'imagen':'static/img/categorias/mouse.jpg',
            },
        ]

    })
    return HttpResponse("Hola Johnsito")

# Vista del home de la página
def home(request):
    request.session['inicial'] = 1
    productos = Producto.objects.all()
    categorias = CategoriaProducto.objects.exclude(pk = 1)
    
    random1 = Producto.objects.order_by('?')[:3]
    random2 = Producto.objects.order_by('?')[:3]
    random3 = Producto.objects.order_by('?')[:3]
    
    return render(request, 'index.html', {
        'producto': productos,
        'categorias': categorias,
        'random1': random1,
        'random2': random2,
        'random3': random3,
        'correo': 'info@softbox190.com',
    })

def quienes_somos(request):
    request.session['inicial'] = 1
    return render(request, 'quienes-somos.html', {
        'titulo':'Quiénes Somos',
        'contenido':"",
    })
    return HttpResponse("Sección De quienes somos!")

def gracias(request):
    request.session['inicial'] = 1
    return render(request, 'gracias.html', {
        'titulo':'Gracias por su compra',
        'contenido':'Hemos enviado a su correo electrónico la confirmación de la compra. Muchas gracias por confiar en nosotros.',
    })
    return HttpResponse("Sección De quienes somos!")

def login(request):
    request.session['inicial'] = 1
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        usuario = authenticate(username=usuario, password=password)
        if usuario:
            lg(request, usuario)
            print("el usuario se ha logueado")
            return redirect('home')
        else:
            print("El usuario no existe")

    return render(request, 'users/login.html', {})

# Función para agregar productos al carrito
def agregarAcarrito(request):
    #del request.session['cartdata']
    carrito = Carrito.objects.filter(session=request.session.session_key)
    
    cart_p = {}
    cart_p[str(request.GET['id'])]={
        'title':request.GET['title'],
        'qty':int(request.GET['qty']),
        'price':request.GET['price'],
        # 'title':request.GET['title'],
    }
    precio = request.GET['price']
    precio = float(precio.replace(",", ".", 1))
        
    if 'cartdata' in request.session:
        cantidad_x_prod = int(request.GET['qty'])
        if str(request.GET['id']) in request.session['cartdata']:
            cart_data = request.session['cartdata']
            cart_data[ str(request.GET['id']) ]['qty'] += int(request.GET['qty'])
            cantidad_x_prod = cart_data[ str(request.GET['id']) ]['qty']
            cart_data.update(cart_data) #actualizamos el producto en cantidad
            request.session['cartdata'] = cart_data
            
            carrito2 = carrito.filter(producto=Producto.objects.get(id=request.GET['id']))
            carrito2.update(precio=precio, cantidad=cantidad_x_prod)
        else:
            cart_data = request.session['cartdata']
            cart_data.update(cart_p) # Agregamos un producto nuevo
            request.session['cartdata'] = cart_data
            carrito.create(session=request.session.session_key, precio=precio, cantidad=int(request.GET['qty']), producto=Producto.objects.get(id=request.GET['id']))
    else:
        
        request.session['cartdata'] = cart_p
        carrito.create(session=request.session.session_key, precio=precio, cantidad=int(request.GET['qty']), producto=Producto.objects.get(id=request.GET['id']))
    #Calculamos total
    carrito = Carrito.objects.filter(session=request.session.session_key)
    cart_total = 0
    for carrito_indv in carrito:
        cart_total += carrito_indv.precio * carrito_indv.cantidad 
    request.session.cart_total = cart_total
        
    return JsonResponse({'data':request.session['cartdata'], 'totalitems':len(request.session['cartdata']), 'cart_total':request.session.cart_total ,})


def eliminarCarritoIndv(request):
    request.session['inicial'] = 1
    id_producto = str(request.GET['id'])
    
    # Eliminamos tanto de la sesión como de la base de datos - tabla carrito
    Carrito.objects.filter(producto_id=Producto.objects.get(id=request.GET['id']), session=request.session.session_key).delete()
    request.session['cartdata'].pop(id_producto)
    
    # Averiguamos cuanto es el total de la compra
    carrito = Carrito.objects.filter(session=request.session.session_key)
    cart_total = 0
    for carrito_indv in carrito:
        cart_total += carrito_indv.precio * carrito_indv.cantidad 
    request.session.cart_total = cart_total
    # Devolvemos el Json
    return JsonResponse({'data': request.session['cartdata'] , 'totalitems':len(request.session['cartdata']) , 'cart_total':request.session.cart_total ,})


# Modificar el carrito
def actualizarElCarrito(request):
    #del request.session['cartdata']
    carrito = Carrito.objects.filter(session=request.session.session_key)
    
    cart_p = {}
    
    return JsonResponse({'data':request.session['cartdata'], 'totalitems':len(request.session['cartdata']),})



#####