from django.db import models

STATE = [
    ('OH', 'On hold'),
    ('IP', 'In preparation'),
    ('FD', 'Finalized'),
]


class State(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    order_state = models.CharField(max_length=2, choices=STATE, default='OH')

    def __str__(self):
        return self.id
