from django.db import models
from course.models import Course

class Lesson(models.Model):
    lesson_id = models.AutoField("Lesson id", unique=True, primary_key=True)
    course = models.ForeignKey(
                            Course, 
                            on_delete=models.CASCADE,
                            verbose_name='id Курса',
    )
    title = models.CharField("Название урока", max_length=30, unique=True)
    preview = models.ImageField("Обложка",
                            upload_to="img/lessons/preview",
                            height_field=None,
                            width_field=None,
                            max_length=120
                            )
    description = models.CharField("Описание", default="Бла-бла", max_length=150)
    lesson_order = models.DecimalField('Порядок', unique=False, max_digits=10, decimal_places=0, default=0)
    
    def __str__(self):
        return self.title