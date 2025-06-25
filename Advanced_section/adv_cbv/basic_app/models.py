from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 255)
    principal = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Incorrect use of Django template tags ({% url ... %}) inside Python code — {% url ... %} is only used in HTML templates,
        #  not in Python code.
        return reverse("basic_app:detail", kwargs = {'pk': self.pk} )


class Student(models.Model):
    name = models.CharField(max_length = 255)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,on_delete = models.CASCADE, related_name = 'students')

    def __str__(self):
        return self.name