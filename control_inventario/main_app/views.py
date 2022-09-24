from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index_login_page(request):
    return render(request, 'users/login.html')

def register_page(request):
    return render(request, 'users/register.html', {
        'title': 'Registro de usuario'
    })
