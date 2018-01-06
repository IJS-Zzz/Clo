from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #Вывод простого HTML кода


# ==== lesson ====
def home(request):
    # рендер страницы HTML
    return render(request, 'lesson/homePage.html')

def contact(request):
    # рендер страницы HTML
    return render(request, 'lesson/contact.html',
        {
            'values':
                ['Привет!',
                'Если у вас остались вопросы, то можете задать их мне по телефону',
                '(068) 068-68-68',
                'mail@clo.com']
        })