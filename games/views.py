from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #Вывод простого HTML кода


def game(request):
    # рендер страницы HTML
    return render(request, 'games/game.html')
