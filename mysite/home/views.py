from django.shortcuts import render

# Create your views here.
def HomeView(request):
    '''Página principal'''
    # retornamos una http con la plantilla index.html y los objetos de la base de datos
    return render(request, "index.html")

def ProductView(request):
    '''Infromación del producto'''
    return render(request, "about/producto.html")

def ContactView(request):
    '''Nosotros y Contacto'''
    return render(request, "nosotros.html")

def FaqView(request):
    '''Nosotros y Contacto'''
    return render(request, "about/faq.html")
