from django.shortcuts import render, HttpResponse

# Create your views here.
def lista_compras(request):
    return render(request, "gastos_operacionales.html")