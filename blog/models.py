from django.db import models

# Create your models here.


class Malumot(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='index/img')
    bio = models.TextField()

    def __str__(self):
        return self.name



class Kansultatsiya(models.Model):
    name = models.CharField(max_length=200)
    phonenumber = models.IntegerField()

    def __str__(self):
        return self.name



class Yonalish(models.Model):
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.bio


class Kids(models.Model):
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.bio


class Student(models.Model):
    img  = models.ImageField(upload_to='index/img')



class Carusel(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name











































