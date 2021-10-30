from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import login as lg
from django.contrib.auth import authenticate
from django.shortcuts import redirect

def saludo(request):
    return render(request, 'index.html', {
        'mensaje': 'Bienvenidos a nuestro proyecto',
        'nombres': [1, 2, 3, 4, 'John'],
        'suma': 5 + 3,
        'alumnos': [
            {
                'nombre': 'Allison',
                'edad': '27',
                'aprobo': True,
            },
            {
                'nombre': 'John',
                'edad': '33',
                'aprobo': True,
            },
            {
                'nombre': 'Milo',
                'edad': '2',
                'aprobo': True,
            },
        ],
        'saludo': 'Buenas!',
        'slider': [
            {
                'src':'img/fotografo-paisajes.jpeg',
                'class':'d-block w-100',
                'alt':'Descripción de foto 1',
                'activo':True,
            },
            {
                'src':'img/lago-paisaje.jpeg',
                'class':'d-block w-100',
                'alt':'Descripción de foto 2',
                'activo':False,
            },
            {
                'src':'img/luna-atardecer.jpg',
                'class':'d-block w-100',
                'alt':'Descripción de foto 3',
                'activo':False,
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