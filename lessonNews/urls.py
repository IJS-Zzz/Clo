from django.urls import path

# Библеотека которая работает со списком,
# который сформирован и полечен от база данных SQL
from django.views.generic import ListView, DetailView
from lessonNews.models import Articles

# from . import views


app_name = 'lessonNews'
urlpatterns = [

    # /lessonNews/ - отображает все статьи,
    # которые есть в базе данных с помощью метода:
    #   ListView - отображение html с for, работа со списком
    #   |        as_view - запрос к базе данных
    #   |        |       queryset - запрос
    #   |        |       |        Articles - название таблицы в БД
    #   |        |       |        |        objects - то, что нам нужен отбъект базы данных
    #   |        |       |        |        |       all() - все объекты
    #   |        |       |        |        |       |     order_by - метод сортировки
    #   |        |       |        |        |       |     |        (.......) - по какому параметру
    #   |        |       |        |        |       |     |         "date" - начиная со старых новостей
    #   |        |       |        |        |       |     |         "-date" - начиная с новых новостей
    #   |        |       |        |        |       |     |                 [:x] - срез строки, первые x статей
    path('', 
        ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
        template_name="lessonNews/posts.html")),
    #   |
    #   template_name - указывает какой шаблон нам нужно брать
    #                                                                 -----------------
    #   метод ListView возвращает в html шаблон список в виде объекта | 'object_list' |
    #                                                                 -----------------

    #   DetailView - отображение конкретной модели
    path('<int:pk>/',
        DetailView.as_view(model=Articles,
            template_name="lessonNews/post.html"))

]