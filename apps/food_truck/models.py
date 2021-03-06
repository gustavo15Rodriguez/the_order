from django.db import models
from apps.product.models import Product


class FoodTruck(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='static/images', default='static/images/logo.png')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
