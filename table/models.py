from django.db import models
from django.http import HttpResponse

# Create your models here.
class Task(models.Model):
    week_name = models.CharField(max_length=20)
    task = models.TextField()

    def __str__(self):
        return f"{self.task}"