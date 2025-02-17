from django.shortcuts import render

# Create your views here.
def HomeView(request):
    '''Página principal'''
    # retornamos una http con la plantilla index.html y los objetos de la base de datos
    return render(request, "index.html")
