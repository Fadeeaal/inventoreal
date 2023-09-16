from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    creator = models.CharField(max_length=255)
    npm = models.CharField(max_length=255)
    pbpclass = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.TextField(default=" ")
    price = models.IntegerField()
    amount = models.IntegerField()