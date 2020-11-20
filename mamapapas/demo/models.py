from django.db import models

# Create your models here.

class Demo(models.Model):
    title = models.CharField('Пометки', max_length=50)
    content = models.TextField('Содержание урока', max_length=1000000,)
    is_last = models.BooleanField('Последняя ли страница', default=False)
    order = models.DecimalField('Порядок', unique=False, max_digits=10, decimal_places=0, default=0)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return "/courses/demo/{self.order}/"