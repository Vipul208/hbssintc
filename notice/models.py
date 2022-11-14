
from turtle import left, position
from django.db import models


# Create your views here.

class noticeboard(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()


class galleries(models.Model):
    image = models.ImageField(upload_to="gal")


class teacher(models.Model):
    position= models.IntegerField()
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=20)
    image = models.ImageField(upload_to="teacher")
    mail = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)


class testimonial(models.Model):
    name = models.CharField(max_length=30)
    heading = models.CharField(max_length=50)
    dis = models.TextField()
    img = models.ImageField(upload_to="pics")
