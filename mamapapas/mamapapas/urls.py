from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# Лендинг
from page.views import (home_view, 
                        payment_course1_view, 
                        payment_course2_view, 
                        payment_course3_view, 
                        payment_course_full_view,
                        privacy_view,
)

# Личный кабинет
from course.views import courses_view, course_name_view # Также относится и к лендингу
from payment.views import changestatus

# Контент
from content.views import content_view
from demo.views import demo_view

# Тесты
from test.views import tests_view

# Файлы для скачивания
from coursefile.views import coursefile_view

# Чаты
from django_private_chat import urls as django_private_chat_urls

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('course/', courses_view, name='course'),
    path('course/<int:course_id>/', course_name_view, name='course_name'),
    path('account/', include('allauth.urls')),
    path('privacy/', privacy_view, name='privacy'),

    # вывод контента
    path('course/<int:course_id>/<int:lesson_id>/content/<int:order>/', content_view, name='content'),
    path('demo/<int:order>/', demo_view, name='demo'),

    # тесты
    path('course/<int:course_id>/<int:lesson_id>/test/<int:test_id>/', tests_view, name='tests_name'),

    # транзакции
    path('success/course1/', payment_course1_view, name='Транзация первого курса'),
    path('success/course2/', payment_course2_view, name='Транзация второго курса'),
    path('success/course3/', payment_course3_view, name='Транзация третьего курса'),
    path('success/full_course/', payment_course_full_view, name='Транзация полного курса'),

    # файлы для скачивания
    path('course/files', coursefile_view, name='Файлы для скачивания'),

    # чат
    path('', include('django_private_chat.urls')),
] + static('/media/', document_root=settings.MEDIA_ROOT) + static('/static/', document_root=settings.STATIC_ROOT)
