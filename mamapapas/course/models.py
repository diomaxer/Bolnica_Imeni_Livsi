from django.db import models

class Course(models.Model):
    course_id = models.AutoField("Course id", unique=True, primary_key=True)
    title = models.CharField("Название", max_length=30, unique=True)
    preview = models.FileField("Обложка (розовая иконка #FDB2D5)", upload_to="img/courses", max_length=120)
    icon = models.FileField("Иконка (светло-серая иконка #ECECEC)", upload_to="img/courses/icons", max_length=120)
    description = models.CharField("Описание", default="Бла-бла", max_length=150)
    fulldescription = models.TextField("Полное описание", default="Бла-бла-бла", max_length=5000)
    price = models.DecimalField("Цена", decimal_places=0, max_digits=50)
    course_order = models.DecimalField("Порядок курса", decimal_places=0, max_digits=10, default=0)
    
    def __str__(self):
        return self.title

    def half_sale(self):
        price = int(self.price / 2)
        return price

    def get_absolute_url(self):
        return "/courses/{self.course_id}/"