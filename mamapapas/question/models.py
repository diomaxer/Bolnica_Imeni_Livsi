from django.db import models
from django import template

from answer.models import Answer


class Question(models.Model):
    question_id = models.AutoField("Question id", unique=True, primary_key=True)
    title = models.CharField('Заголовок вопроса', max_length=255, blank=False, default='Введите вопрос')
    answer = models.ManyToManyField(Answer)
    explanation = models.CharField('Объяснение правильного ответа', max_length=5000,blank=True)
    question_image = models.ImageField("Картинка к вопросу",
                                    upload_to="img/lessons/questions",
                                    height_field=None,
                                    width_field=None,
                                    max_length=120,
                                    blank=True,
    )

    def __str__(self):
        return self.title
