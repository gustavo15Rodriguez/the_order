from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=15)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='static/images', default='static/images/product.png')
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
