from django.db import models

# Create your models here.

class Division(models.Model):
    name = models.CharField(max_length=50)
    population = models.IntegerField()
    area = models.IntegerField()

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=50)
    education_rate = models.IntegerField()
    population_density = models.IntegerField(blank=True, null=True)
    visited = models.BooleanField(default=False)
    division = models.ForeignKey(Division)

    def __str__(self):
        return self.name
