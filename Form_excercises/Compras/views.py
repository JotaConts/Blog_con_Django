from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("<h1>Pagina de inicio de formularios</h1>")
