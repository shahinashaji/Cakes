from django.db import models

# Create your models here.

CATEGORY = (('balck forest', 'Black Forest'),
            ('white forest', 'White Forest'),
            ('red velvet', 'Red Velvet'),
            ('chocolate', 'Chocolate'))


class Cake(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY, max_length=50)
    image = models.ImageField(default=0)

    def __str__(self):
        return self.name
