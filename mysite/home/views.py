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
            'title': 'PYMEs',
            
            'description': 'Restaurantes y Cafeterías'
            "Tiendas de Ropa, Calzado y GYM's"
            'Talleres de Reparación'
            'Estudios de Diseño y Publicidad'
            'Salones de Belleza'
            'Tiendas de Fármacos'
            'Tiendas de Tecnología y Electrónica'
            'Productores y Distribuidores Locales de Alimentos',
            
            'image': 'images/casos-uso/retail.jpg'
        },
        {
            'title': 'Almacenes y centros de distribución',
            
            'description': 'Almacenes de Ropa y Textiles'  
            'Distribuidores de Materiales de Construcción'
            'Centros de Distribución de Alimentos Frescos' 
            'Almacenes de Libros y Material Educativo' 
            'Almacenes de Productos Cosméticos y de Higiene' 
            'Distribuidores de Bebidas y Alimentos Procesados' 
            'Centros de Distribución de Videojuegos y Accesorios',

            
            'image': 'images/casos-uso/warehouse.jpg'
        },
        {
            'title': 'Espacios sociales',
            
            'description': 
            'Salas de Conciertos'
            'Estadios y Arenas'
            'Teatros y Auditorios'
            'Carpas para Eventos y Festivales'
            'Centros de Convenciones'
            'Cines y Espacios para Estrenos',

            'image': 'images/casos-uso/mall.jpg'
        },
        {
            'title': 'Espacios institucionales',
                       
            'description':
            'Gobierno y Administración Pública'
            'Instituciones de Salud y Clínicas'
            'Instituciones Educativas y Universidades'
            'Instituciones Judiciales y Tribunales'
            'Instituciones Financieras y Bancos'
            'Instituciones Corporativas y Oficinas'
            'Organismos Internacionales y ONGs'
            'Centros Culturales y Museos',
            
            'image': 'images/casos-uso/museum.jpg'
        },
        {
            'title': 'Entornos empresariales',
            
            'description': 
            'Oficinas Corporativas'
            'Parques Empresariales'
            'Zonas Industriales'
            'Centros de Negocios'
            'Empresas Tecnológicas y Startups'
            'Centros de Innovación e Investigación'
            'Espacios de Co-working'
            'Empresas de Servicios Profesionales',
            
            'image': 'images/casos-uso/office.jpg'
        }
    ]
    return render(request, "about/casouso.html", {'use_cases': use_cases})
