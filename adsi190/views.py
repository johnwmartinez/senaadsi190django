from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import login as lg
from django.contrib.auth import authenticate
from django.shortcuts import redirect

def saludo(request):
    return render(request, 'index.html', {
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


def login(request):

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