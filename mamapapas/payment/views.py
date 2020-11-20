from django.shortcuts import render

# Create your views here.
from django.db import DatabaseError, transaction
from user.models import User


def changestatus(request, *args, **kwargs):
    user.is_course1 = True 
    user = user.save()
    mumble = 'kkk'
    return render(request, 'courses.html', mumble)