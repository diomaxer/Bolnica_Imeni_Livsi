from django.db import models


class Coursefile(models.Model):
    coursefile_id = models.AutoField("Course file id", unique=True, primary_key=True)
    title = models.CharField("Название файла", max_length=300, unique=True)
    coursefile = models.FileField(upload_to="media/coursefile/")
    coursefile_order = models.DecimalField('Порядок', unique=False, max_digits=10, decimal_places=0, default=0)
    
    def __str__(self):
        return self.title