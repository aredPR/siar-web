from django.shortcuts import render

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
            'title': 'Tiendas minoristas y Comercios',
            'description': 'Instala lectores RFID en la entrada/salida de tu tienda para detectar salidas no autorizadas de productos. Ideal para papelerías, boutiques, tiendas de electrónica y más.',
            'image': 'images/retail.jpg'
        },
        {
            'title': 'Almacenes y Centros de Distribución',
            'description': 'Monitoreo del movimiento de inventario en entradas y salidas para asegurar que los productos no sean retirados sin autorización.',
            'image': 'images/warehouse.jpg'
        },
        {
            'title': 'Supermercados y Centros Comerciales',
            'description': 'Control en puntos estratégicos de acceso, minimizando el hurto de mercancía en áreas de alto flujo.',
            'image': 'images/mall.jpg'
        },
        {
            'title': 'Exposiciones, Ferias y Museos',
            'description': 'Protección de productos de alto valor o piezas en exhibición mediante lectores RFID que controlan su salida.',
            'image': 'images/museum.jpg'
        },
        {
            'title': 'Oficinas y Entornos Empresariales',
            'description': 'Supervisión de equipos y suministros costosos para prevenir robos internos.',
            'image': 'images/office.jpg'
        }
    ]
    return render(request, "about/casouso.html", {'use_cases': use_cases})
