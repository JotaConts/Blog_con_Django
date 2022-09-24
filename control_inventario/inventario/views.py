from curses.ascii import HT
from django.shortcuts import render, HttpResponse

# Create your views here.
def inventario(request):
    return render(request, "inventario.html")
    