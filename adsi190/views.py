from django.http import HttpResponse
from django.shortcuts import render

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
                'aprobo': False,
            },
            {
                'nombre': 'Milo',
                'edad': '2',
                'aprobo': True,
            },
        ],
        'saludo': 'Buenas!',
    })
    return HttpResponse("Hola Johnsito")
