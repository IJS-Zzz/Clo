from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #Вывод простого HTML кода


def index(request):
    # рендер страницы HTML
    return render(request, 'mainApp/index.html')


def contacts(request):
    # рендер страницы HTML
    return render(request, 'mainApp/contacts.html')


def catalog(request):
    # рендер страницы HTML
    return render(request, 'mainApp/catalog.html')

def catalog_blue_dress(request):
    # рендер страницы HTML
    return render(request, 'mainApp/catalog/blue_dress.html')

def catalog_red_dress(request):
    # рендер страницы HTML
    return render(request, 'mainApp/catalog/red_dress.html')

def catalog_jacket(request):
    # рендер страницы HTML
    return render(request, 'mainApp/catalog/jacket.html')

