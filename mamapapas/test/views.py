import datetime

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.db import models
from django.template import RequestContext
from django.contrib.messages import constants as messages
from django.contrib import messages

from test.models import Test
from lesson.models import Lesson
from question.models import Question
from answer.models import Answer
from course.models import Course
from content.models import Content
from user.models import User


def tests_view(request, course_id, lesson_id, test_id, *args, **kwargs):
    user = request.user
    lesson = Lesson.objects.get(lesson_id=lesson_id)
    title = Lesson.objects.get(lesson_id=lesson_id).title
    #question = Question.objects.filter(test_id=test_id)
    #question = Test.objects.filter(question__question_id=1).distinct()
    question = Test.objects.get(test_id=test_id).question.filter()
    #question = Question.objects.filter()
    course_id = Course.objects.get(course_id=course_id).course_id
    #last = Content.objects.filter(course_id=course_id, lesson_id=lesson_id).values_list(flat=True)
    last = Content.objects.filter(course_id=course_id, lesson_id=lesson_id).count()
    pages = Content.objects.filter(course_id=course_id, lesson_id=lesson_id).order_by('order')

    progress = user.lessons_completed.all()

    lesson_order = lesson.lesson_order
    increment = lesson_order + 1

    results = request.POST.getlist('checks[]')
    user = request.user

    if user.is_authenticated:
        try:
            permissions  = user.permissions.all()
        except: 
            permissions = 0
    else:
        permissions = 0
        progress = 0

    lessonlist = Lesson.objects.filter(course_id=course_id).order_by('lesson_order').reverse
    current_lesson = Lesson.objects.get(course_id=course_id, lesson_order=lesson_order)
    last_lesson = lessonlist()[0]

    class UserstatusManager(models.Manager):
        if request.method == 'POST':
            if user.is_authenticated:
                if current_lesson == last_lesson:
                    messages.add_message(request, messages.INFO, 'Курс пройден. Мы выслали на Вашу почту сертификат о его окончании. Ваши мамапапас!')
                    sender = 'no-reply@mamapapas.club'
                    subject_admin = 'Сертификат'
                    message_admin = 'Выдан пользователю '+user.email
                    recipients_admin = ['mamapapasclub@yandex.ru']
                    if message_admin:
                        recipients_admin.append(sender)
                    send_mail(subject_admin, message_admin, sender, recipients_admin)
                    
                    lessons_count = Lesson.objects.count()
                    completed_count = user.lessons_completed.all().count()
                    if lessons_count == completed_count:
                        subject_user = 'Сертификат о прохождении полного курса mamapapas'
                        message_user = loader.render_to_string(
                            'email/cert_full.html',
                            {
                                'first_name': str(user.first_name),
                                'course_name': str(Course.objects.get(course_id=course_id).title),
                                'date_time': str(datetime.date.today()),
                            }
                        )
                    else:
                        subject_user = 'Сертификат mamapapas о прохождении курса '+Course.objects.get(course_id=course_id).title
                        message_user = loader.render_to_string(
                            'email/cert_course.html',
                            {
                                'first_name': str(user.first_name),
                                'course_name': str(Course.objects.get(course_id=course_id).title),
                                'date_time': str(datetime.date.today()),
                            }
                        )
                    recipients_user = [user.email]
                    if message_user:
                        recipients_user.append(sender)
                    send_mail(subject_user, message_user, sender, recipients_user, fail_silently=True, html_message=message_user)
                else:
                    progress = user.lessons_completed.add(Lesson.objects.filter(course_id=course_id).get(lesson_order=lesson_order+1))

                    messages.add_message(request, messages.INFO, 'Результаты теста успешно отправлены. Открыт доступ к следующему уроку')
                    user.save()
            else:
                ...

    my_context = {
        'title' : title,
        'question' : question,
        'course_id' : course_id,
        'last' : last,
        'pages' : pages,
        'course' : Course.objects.get(course_id=course_id),
        'permissions' : permissions,
        'progress' : progress,
        'lesson' : lesson,
    }

    return render(request, 'courses/lessontest.html', my_context)