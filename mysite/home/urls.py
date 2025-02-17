from django.urls import path
from .views import HomeView

urlpatterns = [
    # El parámetro name le asignamos un nombre para llamar a nuestra ruta
    # Así si cambiamos la ruta de "/" a hola/ el nombre seguira indicando la ruta
    path('', HomeView, name="HomeName") # Ruta principal y cargamos Home
]