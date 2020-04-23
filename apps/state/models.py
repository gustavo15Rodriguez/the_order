from django.db import models


class State(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    on_hold = models.BooleanField(default=True)
    in_preparation = models.BooleanField(default=False)
    finalized = models.BooleanField(default=False)

    def __str__(self):
        return self.finalized
