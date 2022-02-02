from django.db import models
from django.utils import timezone

class Claster(models.Model):
    NameClaster = models.CharField(max_length=100,)

    def __str__(self):
        return self.NameClaster

class Project(models.Model):
    cluster = models.ForeignKey(
        'Claster',
        on_delete=models.CASCADE,
    )
    nameProject= models.CharField(max_length=60)
    course = models.CharField(max_length=4)
    discription = models.TextField()
    jobs = models.TextField()
    supervisor = models.CharField(max_length=150)
    contact = models.CharField(max_length=110)
    image = models.FileField(upload_to="путь")

    def __str__(self):
        return self.nameProject
