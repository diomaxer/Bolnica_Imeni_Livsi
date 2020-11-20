from django.shortcuts import render
from django.http import HttpResponse

from .models import Course
from user.models import User

from lesson.models import Lesson

from django.db import DatabaseError, transaction


def courses_view(request, *args, **kwargs):
    user = request.user

    if request.user.is_authenticated:
        progress = user.lessons_completed.all()
        try:
            permissions  = user.permissions.all()
        except:
            permissions = 0
    else:
        progress = 0
        permissions = 0

    courses = Course.objects.filter().order_by('course_order')
    lessons = Lesson.objects.filter()

    my_context = {
        'title' : 'Личный кабинет mamapapas',
        'courses' : courses,
        'permissions' : permissions,
        'lessons' : lessons,
        'progress' : progress,
    }

    return render(request, 'courses/courses.html', my_context)

def course_name_view(request, course_id, *args, **kwargs):
    title = 'Выбор урока'
    lessons = Lesson.objects.filter(course_id=course_id).order_by('lesson_order')
    first_lesson = lessons.get(lesson_order=1)
    user = request.user

    if request.user.is_authenticated:
        progress_start = user.lessons_completed.add(first_lesson)
        progress = user.lessons_completed.filter(course_id=course_id)
        progress_list = user.lessons_completed.all()
        try:
            permissions = user.permissions.all()
        except: 
            permissions = 0
            progress_list = 0
    else:
        progress_list = 0
        permissions = 0

    my_context = {
        'title' : title,
        'lessons' : lessons,
        'course' : Course.objects.get(course_id=course_id),
        'permissions' : permissions,
        'progress_list' : progress_list,
        'progress' : progress,
    }
    
    return render(request, 'courses/lessons.html', my_context)