from django.db import models


class Review(models.Model):
    review_id       = models.AutoField("Review id", unique=True, primary_key=True)
    preview         = models.FileField("Скриншот", upload_to="img/reviews", max_length=120)
    review_order    = models.DecimalField("Порядок Отзыва", decimal_places=0, max_digits=10, default=0)
    def __str__(self):
        return str(self.review_order)