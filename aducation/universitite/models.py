from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, null=False)
    group = models.CharField(max_length=50, null=False)
    nomer = models.CharField(max_length=13, null=False)
    age = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100, null=False)
    nomer = models.CharField(max_length=13, null=False)
    age = models.IntegerField(null=False)

    def __str__(self):
        return self.name,self.age,self.nomer





