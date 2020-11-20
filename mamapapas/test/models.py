from django.db import models
from django import template

from lesson.models import Lesson 
from question.models import Question


class Test(models.Model):
    test_id = models.AutoField("Test id", unique=True, primary_key=True)
    title = models.CharField('Заголовок теста', max_length=255, blank=False, default='Введите заголовок')
    lesson = models.ForeignKey(
        Lesson, 
        on_delete=models.CASCADE,
        verbose_name='Урок',
    )
    question = models.ManyToManyField(Question)

    def __str__(self):
        return f'"{self.title}" к уроку "{self.lesson}"'