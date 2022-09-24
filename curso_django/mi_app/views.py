from django.shortcuts import redirect, render, HttpResponse
from mi_app.models import Article
from mi_app.forms import Form_article
from django.db.models import Q
from django.contrib import messages

# APUNTES IMPORTANTES!!

# ETAPA 1:
# 1) Creación de vistas básicas
# 2) Configuración de un encabezado:
#       - Creación de varialble que contenga todo el codigo html
#       - Insersión de la avariable "layout" en todas las vistas
# 3) Configuración de una vista para recibir parámetros
# 4) Redirección a otra url usando redirect (no aplicado aún)

# ETAPA 2:
# 5) Uso de templates para desarrollar el html separado de las vistas
#       - Layout: será el molde de nuestra web
#       - Habrá {% bloques %} para cargar contenido específico desde cada template
#       - Cada template heredará el {% extends 'layout.html' %} y tb cargará su contenido específico.

# ETAPA 3: (PENDIENTE)
# 6) Dar estilo con html y css a la página

# ETAPA 4:
# 7) Lenguaje de plantillas/template
#       - Pasar variables desde las views al template (ver years.html)
#       - Creación de condicionales y bucles en el template con variables declaradas en views
#       
#       - <% include %> : Con la instrucción include puedo insertar un template dentro de otro template.
#           · De esta manera creamos pequeños trozos de template con su funcionalidad específica
#           · y luego lo incluimos dentro del template oficial (ver ejemplo en years_2.html)
#       
#       - <% url %> : Con esta instrucción podemos redireccionar usando el 'name' de alguna de nuestras urls.
#       - Si la url recibe parámetros, podemos entregárselos a continuación del nombre:
#               <% url 'years_2' 'Jota' 'Contreras' %>
#               <% url 'years_2' name='Jota' apellido= 'Contreras' %>
#       - Si el nombre de la ruta cambia, no habrá problema porque el template está relacionado a través del 'name'
#       - Para uso de <% url %> ver layout.html
#
# 8) Lenguaje de plantillas: filters/filtros:
#       - Uso de filtros (funcionalidades)
#       - Ver todos los filtros y su uso en https://docs.djangoproject.com/en/4.0/ref/templates/builtins/

# ETAPA 5:
# 9) Modelos (bd): Creación de un blog
#       - En models.py (ver) se crean las clases para cada modelo de datos.
#       - En views.py (ver) creamos una nueva vista: crear_articulo
#       - Importamos los modelos al comienzo del views.py
#       - En url creamos el path crear_articulo.
#       - Al path agregamos los parámetros que queremos para la creación del artículo.

# 10) Obtener datos desde la bd:
#       - Creamos una nueva vista articulos (creamos el path en views.py)
#       - Instanciamos un objeto Article.objects.get()
#           · objects nos permite acceder a los objetos de la bd
#           · get() nos permite obtener un dato dandole un parámetro
#           · all() nos permite obtener todos los datos de la tabla

# 11) Crear Formularios:
#       - Ver funcion nuevo_articulo y save_articulo

# ----- 1) Vistas de configuración básica:-----
# Retornar un mensaje en html (muy básico)
def index(request):
    return HttpResponse("<h1>Inicio</h1>")

def saludo(request):
    return HttpResponse("""
    <h1>Aprendiendo Django</h1>
    <h3>Soy Jota Contreras<h/3>
    """)

# Retornar el mensaje html a través de una variable:
def pagina(request):
    html = """
    <h1>Pagina web</h1>
    <p>Creada por Jota</p>
    <ul>
    """
    return HttpResponse(html)

# Crear un script (bucle) para mostar info por pantalla:
def years(request):
    html = """
    <h1>Indice de años</h1>
    <p>Años hasta el 2050:</p>
    """
    year = 2022
    while year <= 2050:
        html += f"<li>{str(year)}</li>"
        year += 1
    html += "</ul>"
    return HttpResponse(html)


# ----- 2) Configurar un encabezado para ser insertado en varias vistas:-----

layout = """
<h1>jotacontreras.com</h1>
</hr>
<ul>
    <li>
    <a href="/intranet">Intranet</a>
    </li>
    <li>
    <a href="/info">Info</a>
    </li>
    <li>
    <a href="/contacto">Contacto</a>
    </li>
</hr>
</ul>
"""

def intranet(request):
    return HttpResponse(layout+"<h1>Intranet</h1>")


def info(request):
    return HttpResponse(layout+"<h1>Página de intranet</h1>")


def contacto(request):
    return HttpResponse(layout+"<h1>jota@jota.cl</h1>")

# ----- 3) Configurar recepción de parámetros por url-----

def agenda(request, nombre="Invitado", apellido=""):
    return HttpResponse(layout+f"<h1>Bienvenido {nombre} {apellido}</h1>")


# ----- 5) Usar templates separados de las views-----

def index_2(request):
    return render(request, 'index_2.html')

def saludo_2(request):
    return render(request, 'saludo_2.html')

def pagina_2(request):
    return render(request, 'pagina_2.html')

# ----- 7) Lenguaje de plantillas/templates-----

# Esta función la redefiniremos creando el bucle en la plantilla:

def years_2(request):
    """
    html = ""
    <h1>Indice de años</h1>
    <p>Años hasta el 2050:</p>
    ""
    year = 2022
    while year <= 2050:
        html += f"<li>{str(year)}</li>"
        year += 1
    html += "</ul>"
    return render(request, 'years_2.html')
    """

    year = 2022
    until = range(year, 2051)
    # Le pasamos un dict indicando la variable que usaremos ('until')
    return render(request, 'years_2.html', {'year_list':until})

# ----- 8 y 9) Modelos (db) -----

def crear_articulo(request, title, content, public):
    # Creamos un objeto tipo Article y le damos los parámetros:
    mi_articulo = Article(
        title=title,
        content=content,
        public=public
    )
    # Confirmamos los cambios:
    mi_articulo.save()
    return HttpResponse(f"Articulo creado: {mi_articulo.title}: <p>{mi_articulo.content}</p>")

def buscar_articulo(request):
    try:
        #articulo = Article.objects.get(pk=3)
        articulo = Article.objects.get(title="post_2")
        response = f"<h3>Articulo: {articulo.title}</h3><p>{articulo.content}</p>"
        return HttpResponse(response)
    except:
        return HttpResponse("Articulo no encontrado")

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = False
    articulo.save()
    return HttpResponse(f"Articulo editado: <strong>{articulo.id}-{articulo.title}</strong>")


# En la sgte función veremos ejemplos de consultas con el ORM (sorting, filter, lookups)
# y de querys en SQL

def mis_articulos(request):
    # con all() obtenemos todos los articulos:
    articulos = Article.objects.all()

    # con order_by obtenemos los articulos por orden según se indique:
    #articulos = Article.objects.order_by('created_at')[:6]

    # con filter podemos decidir cuáles articulos mostrar según nuestra query
    # podemos filtrar por rango de id, por titluo exacto, por titulo parcial, etc:
    
    # por rango de id usaremos:
    # gt (greater than), gte (greater than equal), lt (less than), lte (less than equal) 
    #articulos = Article.objects.filter(id__gte=3, id_lte=9)

    # por titulo exacto (__exact)
    # por titulo exacto sin case sensitive (__iexact)
    # por titulo parcial (__contains)
    #articulos = Article.objects.filter(title__iexact="batman")

    # para usar condición OR (|) --> from django.db.models import Q
    #articulos = Article.objects.filter(Q(title__contains="batman") | Q(title__contains="post"))

    # excluir de la selección según una condicion:
    # .exclude(condicion)
    #articulos = Article.objects.filter(id__gte=1).exclude(public=False)

    # consultas SQL (.raw)
    #articulos = Article.objects.raw("SELECT * FROM mi_app_article WHERE title = 'Batman'")

    return render(request, 'mis_articulos.html', {'articulos':articulos})
    # para que el html use la variable articulos, se la entregamos a través de un dict
    # en mis-articulos.html debemos hacer un <% for %> para recorrer el objeto 

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('mis_articulos')

# ----- 10) Formularios -----
def guardar_articulo(request):

    if request.method == 'POST':
        title=request.POST['title']
        content=request.POST['content']
        public=request.POST['public']
        # Creamos un objeto tipo Article y le damos los parámetros:
        mi_articulo = Article(
            title=title,
            content=content,
            public= public
        )
        # Confirmamos los cambios:
        mi_articulo.save()
        return HttpResponse(f"Articulo creado: {mi_articulo.title}: <p>{mi_articulo.content}</p>")
    
    else:
        return HttpResponse("<h2>No se pudo Guardar el artículo</h2>")


def nuevo_articulo(request):
    return render(request, 'nuevo_articulo.html')

# Formulario hecho con clases (poo)
def nuevo_objeto_articulo(request):
    
    if request.method == 'POST':
        formulario  = Form_article(request.POST)
    
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form['title']
            content = data_form['content']
            public = data_form['public'] #obtener la info de otra forma, funciona igual que .get

            mi_articulo = Article(
            title=title,
            content=content,
            public=public
            )

            # Mensaje flash (se muestra una vez)
            messages.success(request, f'Se ha creado tu articulo {mi_articulo.title}')
            mi_articulo.save()

            #return HttpResponse(f"{mi_articulo.title} - {mi_articulo.content} - {str(mi_articulo.public)}")
            return redirect('mis_articulos')
    else:
        formulario = Form_article()
    
    return render(request, 'nuevo_objeto_articulo.html', {
        'form': formulario
        })

