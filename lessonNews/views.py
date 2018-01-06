from django.shortcuts import render
from django.http import HttpResponse #Вывод простого HTML кода

# Create your views here.


# =========== TEST ===================
# from .templates.lesson import page
# страница как переменная page
# из файла "templates/lesson/page.py"

def fuck_u(request):
    return HttpResponse("Fuck U!")
# =========== TEST ===================