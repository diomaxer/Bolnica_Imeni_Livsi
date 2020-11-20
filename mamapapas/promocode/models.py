from django.db import models


class Promo(models.Model):
    name = models.CharField("Новый промокод", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новый промокод'
        verbose_name_plural = 'Новые промокоды'
