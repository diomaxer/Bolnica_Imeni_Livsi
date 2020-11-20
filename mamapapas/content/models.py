from django.db import models

from course.models import Course
from lesson.models import Lesson
# Create your models here.

class Content(models.Model):
    title = models.CharField('Пометки', max_length=50)
    course = models.ForeignKey(
                            Course, 
                            on_delete=models.CASCADE,
                            verbose_name='Курс',
    )
    lesson = models.ForeignKey(
                            Lesson, 
                            on_delete=models.CASCADE,
                            verbose_name='Урок',
    )
    content = models.TextField('Содержание урока', max_length=1000000,)
    order = models.DecimalField('Порядок', unique=False, max_digits=10, decimal_places=0, default=0)
    def __str__(self):
        return self.content
    def get_absolute_url(self):
        return "/courses/{self.course_id}/{self.lesson_order}/{order}"