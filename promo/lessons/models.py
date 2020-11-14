from django.db import models


class Lessons(models.Model):
    name = models.CharField("Урок", max_length=255)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

    def get_sale(self):
        ''' Расчитать стоимость со скидкой '''
        price = int(self.price) / 2
        return price
