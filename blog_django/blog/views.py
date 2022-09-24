from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def list(request):

    articles = Article.objects.all()

    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': articles
    })

@login_required(login_url='login')
def category(request, category_id):
    """
    Normalmente deberíamos entregar el objeto Article para mostrarlo en el html
    Pero como la BD está relacionada a Category (foreing_key), puedo obtener el set de datos
    del objeto Article a través de Category directamente (ver category.html).
    """
    #category = Category.objects.get(id=category_id)
    #articles = Article.objects.filter(categories=category_id)
    category = get_object_or_404(Category, id=category_id)


    return render(request, 'categories/category.html', {
        'category': category,
        #'articles':articles
    })