from django.shortcuts import render

# Create your views here.
from .models import Content
from lesson.models import Lesson
from content.models import Content
from test.models import Test
from course.models import Course

def content_view(request, course_id, lesson_id, order, *args, **kwargs):
    pages = Content.objects.filter(course_id=course_id, lesson_id=lesson_id).order_by('order')
    obj = Content.objects.get(course_id=course_id, lesson_id=lesson_id, order=order)
    title = Lesson.objects.get(course_id=course_id, lesson_id=lesson_id).title
    pagenumber = Content.objects.get(course_id=course_id, lesson_id=lesson_id, order=order).order
    
    # Хорошая идея прописать инкремент и сослаться на него в template
    increment = order + 1
    decrement = order - 1
    user = request.user

    lesson = Lesson.objects.get(lesson_id=lesson_id)
    progress = user.lessons_completed.all()

    #if obj is pages.reverse()[0]:
    #    global last_page
    #    last_page = pages.reverse()[0]
    #else:
    #    last_page = None
    last_page = Content.objects.filter(course_id=course_id, lesson_id=lesson_id).order_by('order').reverse()[0]

    if user.is_authenticated:
        try:
            permissions  = user.permissions.all()
        except: 
            permissions = 0
    else:
        permissions = 0
        #progress = 0

    test = Test.objects.get(lesson_id=lesson_id)
    test_id = Test.objects.get(lesson_id=lesson_id).test_id

    course_id = Course.objects.get(course_id=course_id).course_id

    my_context = {
        'pagenumber'        : pagenumber,
        'title'             : title,
        'increment'         : increment,
        'decrement'         : decrement,
        'obj'               : obj,
        'test'              : test,
        'test_id'           : test_id,
        'course'            : Course.objects.get(course_id=course_id),
        'permissions'       : permissions,
        'course_id'         : course_id,
        'pages'             : pages,
        'progress'          : progress,
        'lesson'            : lesson,
        'last_page'         : last_page,
    }
    return render(request, 'courses/lessonpage.html', my_context)