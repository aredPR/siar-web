from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.urls import reverse

#Vistas de la aplicación

def HomeView(request):
    '''Página principal'''
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

def TecnologiaView(request):
    '''Tecnologia'''
    return render(request, "tecnologia.html")

def LoginView(request):
    '''Iniciar Sesión'''
    return render(request, "login.html")


def CasoUso(request):
    '''Casos de Uso'''
    use_cases = [
        {
            'title': 'PYMEs',
            'description': [
                '✅ Restaurantes y cafeterías',
                '✅ Tiendas de ropa, calzado y GYM\'s',
                '✅ Talleres de reparación',
                '✅ Estudios de diseño y publicidad',
                '✅ Salones de belleza',
                '✅ Tiendas de fármacos',
                '✅ Tiendas de tecnología y electrónica',
                '✅ Productores de alimentos'
            ],
            'image': 'images/retail.jpg'
        },
        {
            'title': 'Almacenes y centros de distribución',
            'description': [
                '✅ Almacenes de ropa y textiles',
                '✅ Distribuidores de materiales',
                '✅ Centros de distribución de alimentos',
                '✅ Almacenes de libros',
                '✅ Almacenes de productos de higiene',
                '✅ Distribuidores de bebidas',
                '✅ Centros de distribución de videojuegos'
            ],
            'image': 'images/warehouse.jpg'
        },
        {
            'title': 'Espacios sociales',
            'description': [
                '✅ Salas de conciertos',
                '✅ Estadios',
                '✅ Teatros y auditorios',
                '✅ Carpas para eventos y festivales',
                '✅ Centros de convenciones',
                '✅ Cines y espacios para estrenos'
            ],
            'image': 'images/concert.jpg'
        },
        {
            'title': 'Espacios institucionales',
            'description': [
                '✅ Gobierno y administración pública',
                '✅ Instituciones de salud y clínicas',
                '✅ Instituciones educativas',
                '✅ Instituciones judiciales y tribunales',
                '✅ Instituciones financieras y bancos',
                '✅ Instituciones corporativas y oficinas',
                '✅ Organismos internacionales y ONGs',
                '✅ Centros culturales y museos'
            ],
            'image': 'images/clinical.jpg'
        },
        {
            'title': 'Entornos empresariales',
            'description': [
                '✅ Oficinas corporativas',
                '✅ Parques empresariales',
                '✅ Zonas industriales',
                '✅ Centros de negocios',
                '✅ Empresas tecnológicas y startups',
                '✅ Centros de innovación e investigación',
                '✅ Espacios de co-working',
                '✅ Empresas de servicios profesionales'
            ],
            'image': 'images/office.jpg'
        },
        {
            'title': 'Ámbito policial',
            'description': [
                '✅ Protección de armas y municiones',
                '✅ Seguridad de vehículos policiales',
                '✅ Seguridad de equipos tácticos',
                '✅ Protección de evidencia',
                '✅ Campos de investigación militar',
                '✅ Campos de entrenamiento',
                '✅ Sala de reuniones militar'
            ],
            'image': 'images/police.jpg'
        }
    ]
    return render(request, "about/casouso.html", {'use_cases': use_cases})

@login_required 
def DashboardView(request):
    '''Vista Dashboard'''
    login_url= reverse('main:acceder')
    context = {
        'user': request.user,
        'login_url': login_url
    }
    return render(request, 'dashboard.html', context)