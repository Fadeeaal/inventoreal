from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField()