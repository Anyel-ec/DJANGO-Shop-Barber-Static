from django.db import models

class Customer(models.Model):
    dni = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone=models.CharField(max_length=10, blank=True,null=True)