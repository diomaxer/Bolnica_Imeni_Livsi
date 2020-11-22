from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django import forms
from django.http import HttpResponseRedirect
from django.template import loader

from course.models import Course
from faq.models import Faq
from review.models import Review

from .forms import ContactForm


def home_view(request, *args, **kwargs):
    form = ContactForm(request.POST)

    if form.is_valid():
        sender = 'no-reply@mamapapas.club'
        subject_admin = 'Сообщение из формы'
        message_admin = 'E-mail: '+form.cleaned_data['email']+' | '+'Имя: '+str(form.cleaned_data['name'])+' | '+'Телефон: '+form.cleaned_data['phone']
        recipients_admin = ['mamapapasclub@yandex.ru']
        if message_admin:
            recipients_admin.append(sender)
        send_mail(subject_admin, message_admin, sender, recipients_admin)

        subject_user = 'Добро пожаловать на мамапапас!'
        message_user = loader.render_to_string(
            'email/hello.html',
            {
                'first_name' : str(form.cleaned_data['name']),
            }
        )
        recipients_user = [form.cleaned_data['email'].lower()]

        if message_user:
            recipients_user.append(sender)
        send_mail(subject_user, message_user, sender, recipients_user, fail_silently=True, html_message=message_user)

        return HttpResponseRedirect('/demo/1')

    my_context = {
        'title' : "Онлайн-школа для беременных MamaPapas.club. Курсы для будущих родителей.",
        'description' : "Добро пожаловать в онлайн-школу MamaPapas.club - на курсы для будущих родителей. MamaPapas.club позаботиться о Вас, пока Вы заботитесь о своем Чуде.",
        'form' : ContactForm,
        'keywords' : "курсы, беременных, ребенок, новорожденный, беременность, роды, школа, онлайн, мама, папа, mamapapas",
        'courses' : Course.objects.filter().order_by('course_order'),
        'faqs' : Faq.objects.filter().order_by('faq_order'),
    	'reviews' : Review.objects.filter().order_by('review_order'),
    }
    return render(request, 'home.html', my_context)


def privacy_view(request, *args, **kwargs):
    my_context  = {
        'title' : 'Политика конфиденциальности',
    }
    return render(request, 'privacy.html', my_context)


def payment_course1_view(request, *args, **kwargs):
    my_context = {
        'title' : "Оплата прошла успешно",
    }
    user = request.user
    my_context  = {
        'title' : 'Ошибка',
        'text' : 'Вы должны зарегистрироваться',
    }
    if user.is_authenticated:
        course = Course.objects.get(course_id=1)
        user.permissions.add(course)
        user.save()
        my_context  = {
            'title' : 'Оплата прошла успешно',
            'text' : 'Вы успешно приобрели курс "Беременность". Добро пожаловать на мамапапас!',
        }
    return render(request, 'success/course2.html', my_context)


def payment_course2_view(request, *args, **kwargs):
    user = request.user
    
    my_context  = {
        'title' : 'Ошибка',
        'text' : 'Вы должны зарегистрироваться',
    }
    if user.is_authenticated:
        course = Course.objects.get(course_id=2)
        user.permissions.add(course)
        user.save()
        my_context  = {
            'title' : 'Оплата прошла успешно',
            'text' : 'Вы успешно приобрели курс "Роды". Добро пожаловать на мамапапас!',
        }
    return render(request, 'success/course2.html', my_context)

def payment_course3_view(request, *args, **kwargs):
    my_context = {
        'title'                     : "Оплата прошла успешно",
    }
    user = request.user
    my_context  = {
        'title'         : 'Ошибка',
        'text'          : 'Вы должны зарегистрироваться',
    }
    if user.is_authenticated:
        course = Course.objects.get(course_id=3)
        user.permissions.add(course)
        user.save()
        my_context  = {
            'title'         : 'Оплата прошла успешно',
            'text'          : 'Вы успешно приобрели курс "Новая жизнь". Добро пожаловать на мамапапас!',
        }
    return render(request, 'success/course2.html', my_context)


def payment_course_full_view(request, *args, **kwargs):
    user = request.user

    if user.is_authenticated:
        course1 = Course.objects.get(course_id=1)
        course2 = Course.objects.get(course_id=2)
        course3 = Course.objects.get(course_id=3)
        user.permissions.add(course1)
        user.permissions.add(course2)
        user.permissions.add(course3)
        user.save()
        
    my_context = {
        'title' : 'Оплата прошла успешно',
        'text' : 'Вы успешно приобрели полный курс Мамапапас. Добро пожаловать!',
    }
    return render(request, 'success/course2.html', my_context)
