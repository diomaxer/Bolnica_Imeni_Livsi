from django.db import models
from course.models import Course 
from django.db import DatabaseError, transaction
from user.models import User

@transaction.atomic
def viewfunc(request):
    do_stuff()
    with transaction.atomic():
        user.is_course1 = True 
        user = user.save()


class Payment(models.Model):
    
    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'