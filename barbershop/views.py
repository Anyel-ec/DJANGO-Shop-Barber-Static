from django.http import HttpResponse
from django.shortcuts import render
from appbarberia.models import Customer

def index(request):
    return render(request,"app.html",
                  {"titulo":"Mi Sitio Web","clientes":clientes})

def dashboard(request):
    clientes = Customer.objects.count()
    return render(request,"dashboard.html",
                  {"titulo":"Barber for mens","clientes":clientes})

def clientes(request):
    clientes = Customer.objects.all()
    return render(request,"clientes.html",
                  {"titulo":"Clientes","clientes":clientes})

def barberos(request):
    return render(request,"barbers.html",
                  {"titulo":"Barberos","barberos":barberos})

def productos(request):
    return render(request,"productos.html",
                  {"titulo":"Productos","productos":productos})