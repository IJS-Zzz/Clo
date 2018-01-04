from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #Вывод простого HTML кода


def index(request):
    # рендер страницы HTML
    return render(request, 'mainApp/homePage.html')


# =========== TEST ===================
from .templates.mainApp import page
# страница как переменная page
# из файла "templates/mainApp/page.py"

def fuck_u(request):
    return HttpResponse("Fuck U!")
    return HttpResponse(page.page)
# =========== TEST ===================