from django.urls import path, include
from . import views


app_name = 'main'

urlpatterns = [
     path('', views.HomeView, name="home"), 
     path('Nosotros/', views.ContactView, name="nosotros"),
     path('Tecnologia/', views.TecnologiaView, name="tecnologia"),
     path('Acceder/', views.LoginView, name="acceder"),
     path('AcercaDe/Producto', views.ProductView, name="producto"),
     path('AcercaDe/PreguntasFrecuentes', views.FaqView, name="faq"),  
     path('AcercaDe/CasoUso', views.CasoUso, name="casouso"),
     path('dashboard/', views.DashboardView, name="dashboard"),
 ]
