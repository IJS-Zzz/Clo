from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fuck/', views.fuck_u, name='fuck_u'), # открыть страницу из файла python сохранённой как перемннная
]