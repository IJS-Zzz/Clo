from django.contrib import admin

from lessonNews.models import Articles
# Register your models here.


# Добавляем класс в панель администратора
admin.site.register(Articles)
