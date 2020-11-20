from django.db import models

class Uploads(models.Model):
    upload_id = models.AutoField("Upload id", unique=True, primary_key=True)
    description = models.CharField("Описание файла", max_length=300, blank=True)
    upload = models.FileField(upload_to="media/")
    
    def __str__(self):
        return str(self.upload)

    class Meta:
        verbose_name_plural = "Uploads"
