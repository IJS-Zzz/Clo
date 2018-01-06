from django.urls import path

from . import views

app_name = 'lessonNews'
urlpatterns = [
    path('', views.fuck_u, name='news'),
]