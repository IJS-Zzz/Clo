from django.urls import path

from . import views

app_name = 'mainApp' # чтобы использовать относительные ссылки типа
                     # {% url 'mainApp:index' %}
urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/blue_dress/', views.catalog_blue_dress, name='catalog_blue_dress'),
    path('catalog/red_dress/', views.catalog_red_dress, name='catalog_red_dress'),
    path('catalog/jacket/', views.catalog_jacket, name='catalog_jacket')
]