from django.db import models

class Item(models.Model):
    creator = models.CharField(max_length=255, default='Rakha Fadil Atmojo')
    npm = models.CharField(max_length=255, default='2206082985')
    pbpclass = models.CharField(max_length=255, default='PBP C')
    name = models.CharField(max_length=255)
    categories = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    amount = models.IntegerField()
    description = models.TextField()
