from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to='uploads',null=True)