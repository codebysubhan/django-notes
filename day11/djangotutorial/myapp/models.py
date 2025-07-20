from django.db import models

# Create your models here

# creating test model
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
# testing code
# stu = Student.objects.get(id=1)
# run migrations and migrate command ?
 

