from django.db import models


class Observations(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    without_sauce = models.BooleanField(default=False)
    with_mustard = models.BooleanField(default=False)
    with_soda = models.BooleanField(default=False)
    h_without_onion = models.BooleanField(default=False)

    def __str__(self):
        return self.id
