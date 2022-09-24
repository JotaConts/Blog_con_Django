from curses.ascii import HT
from django.shortcuts import render, HttpResponse

# Create your views here.
def proyectos_inversion(request):
    return HttpResponse ("<h1>Proyectos de inversión 2023</h1>")