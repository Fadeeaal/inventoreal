from django.db import models

class Item(models.Model):
    creator = models.CharField(max_length=255)
    npm = models.CharField(max_length=255)
    pbpclass = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    amount = models.IntegerField()
    description = models.TextField()