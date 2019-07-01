from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.CharField(max_length=20)
    name = models.charField(max_lenght=100)
    email = models.EmailField()
    contact = models.charField(max_length=15)
    class Meta:
        db_table = "employee"


