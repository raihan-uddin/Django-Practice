from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    cls = models.CharField(max_length=50)

    def __str__(self):
        return self.name