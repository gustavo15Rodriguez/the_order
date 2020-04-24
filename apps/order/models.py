from django.db import models
from apps.product.models import Product

OBSERVATIONS = [
    ('WS', 'Without sauce'),
    ('WM', 'With mustard'),
    ('WSD', 'With soda'),
    ('BWO', 'Burger without onion'),
]


class Order(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()
    observations = models.CharField(max_length=3, choices=OBSERVATIONS, default='WS')

    def __str__(self):
        return self.username
