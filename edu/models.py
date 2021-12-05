from django.contrib.auth.models import User
from django.db import models



class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images')
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username



class Courses(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=125, null=True, blank=True)
    image = models.ImageField(upload_to='cources', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=125, null=True, blank=True)
    image = models.ImageField(upload_to='blogs', null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

# SUCCES STORY HOMEWORK

class Succes_story(models.Model):
    title = models.CharField(max_length=125, null=True, blank=True)
    image = models.ImageField(upload_to='successtory', null=True, blank=True)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.ForeignKey(User, models.CASCADE, null=True, blank=True)
    cources = models.ManyToManyField(Courses,  blank=True)
    name = models.CharField(max_length=125, null=True ,blank=True)
    image = models.ImageField(upload_to='studentimages')

    def __str__(self):
        return self.name

class Payments(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    sum = models.IntegerField(null=True, blank=True)
    created_data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.student.name