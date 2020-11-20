from django.db import models
from django import template


class Answer(models.Model):
    answer_id = models.AutoField("Answer id", unique=True, primary_key=True)
    title = models.CharField('Ответ', max_length=255, blank=False, default='Введите ответ')
    is_true = models.BooleanField('Правильный ли ответ', default=False)

    def __str__(self):
        return self.title
