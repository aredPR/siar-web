from django.urls import path
from . import views

app_name = 'main' # Namespace para la app

urlpatterns = [
    # El parámetro name le asignamos un nombre para llamar a nuestra ruta
    # Así si cambiamos la ruta de "/" a hola/ el nombre seguira indicando la ruta
    path('', views.HomeView, name="home"), # Ruta principal Home
    path('nosotros/', views.ContactView, name="nosotros"), 
]