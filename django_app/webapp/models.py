from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=80)
    variant = models.IntegerField()
    qty = models.IntegerField()
    price = models.FloatField()
    description = models.CharField(max_length=300)
