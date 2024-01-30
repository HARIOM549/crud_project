from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class QueryData(models.Model):
    Query=models.CharField(max_length=200)
    QueryEmail=models.CharField(max_length=200)
    # OrderId=models.CharField(max_length=200,null=True)
