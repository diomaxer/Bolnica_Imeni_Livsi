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


class UsersPromocode(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Новый просокод")
    new_promo = models.CharField('Промокод', max_length=255, blank=True)

    def __str__(self):
        return self.new_promo

    class Meta:
        verbose_name = 'Промокод пользователя'
        verbose_name_plural = 'Промокоды пользователей'
