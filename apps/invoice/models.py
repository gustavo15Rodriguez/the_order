from django.db import models

from apps.order.models import Order


class Invoice(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    information = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.information
