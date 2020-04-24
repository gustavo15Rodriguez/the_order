from django.db import models

from apps.order.models import Order

STATE = [
    ('OH', 'On hold'),
    ('IP', 'In preparation'),
    ('FD', 'Finalized'),
]


class State(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    order_state = models.CharField(max_length=2, choices=STATE, default='OH')
    product = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.id
