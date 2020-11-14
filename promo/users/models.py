from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField('Имя', blank=True, max_length=255)
    phone = models.CharField('Номер телефона', max_length=255)
    promo = models.CharField('Промокод', max_length=255, blank=True)

    def get_promo(self):
        if self.promo == '1234':
            return 'Nice'

