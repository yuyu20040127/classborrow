from django.db import models
from django.db.models.fields import CharField, EmailField
from django.db.models.fields.files import ImageField

class Classrooms(models.Model):
    title = CharField('教室名', max_length=255)
    period = CharField('節次', max_length=255)
    image = ImageField('圖片')

    def __str__(self):
        return "{}: {}".format(self.period, self.title)
