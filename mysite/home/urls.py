from django.urls import path
from . import views

app_name = 'main' # Namespace para la app

urlpatterns = [
    # El parámetro name le asignamos un nombre para llamar a nuestra ruta
    # Así si cambiamos la ruta de "/" a hola/ el nombre seguira indicando la ruta
    path('', views.HomeView, name="home"), # Ruta principal Home
    path('Nosotros/', views.ContactView, name="nosotros"),
    path('Tecnologia/', views.TecnologiaView, name="tecnologia"),
    path('Acceder/', views.LoginView, name="acceder"),
    path('AcercaDe/Producto', views.ProductView, name="producto"),
    path('AcercaDe/PreguntasFrecuentes', views.FaqView, name="faq"),  
    path('AcercaDe/CasoUso', views.CasoUso, name="casouso"),
]