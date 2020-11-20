from django.db import models


class Faq(models.Model):
    faq_id = models.AutoField("Faq id", unique=True, primary_key=True)
    question = models.CharField("Вопрос", max_length=120)
    answer = models.TextField("Ответ", max_length=1000)
    faq_order = models.DecimalField('Порядок', unique=False, max_digits=10, decimal_places=0, default=0)
    
    def __str__(self):
        return self.question
    
