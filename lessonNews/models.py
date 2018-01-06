from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length = 120)
    post = models.TextField()
    date = models.DateTimeField()

    # то как будет возвращаться новость
    # вместо объекта возвращает заголовок
    def __str__(self):
        return self.title