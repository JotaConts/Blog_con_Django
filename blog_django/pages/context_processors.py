# Este archivo de debe agregar a:
# settings.py > OPTIONS > context_processors

from pages.models import Page

def get_pages(request):
    #pages = Page.objects.all()
    # Podríamos capturar todo el objeto con all(), pero es muy pesado de procesar.
    # Usaremos values_list y podremos hacer una selección:
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')

    return {
        'pages': pages
    }