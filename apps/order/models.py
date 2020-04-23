from django.db import models

from apps.observations.models import Observations
from apps.product.models import Product
from apps.state.models import State


class Order(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    state = models.OneToOneField(State, on_delete=models.CASCADE, blank=True, null=True)
    observations = models.ForeignKey(Observations, on_delete=models.CASCADE, blank=True, null=True)
    total_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product

