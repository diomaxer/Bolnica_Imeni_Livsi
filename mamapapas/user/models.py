from django.db import models
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse
from django.shortcuts import render
from course.models import Course
from lesson.models import Lesson

class User(AbstractUser):
    first_name = models.CharField('Имя', blank=True, max_length=255)
    phone = models.CharField('Номер телефона', max_length=255)
    promo = models.CharField('Промокод', max_length=255, blank=True)
    permissions = models.ManyToManyField(
                                        Course,
                                        verbose_name='Доступ к курсам',
                                        blank=True,
    )
    lessons_completed = models.ManyToManyField(
                                            Lesson,
                                            verbose_name='Пройденные уроки',
                                            blank=True,
    )


