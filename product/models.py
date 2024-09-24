from django.db import models


class Product(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    marja = models.IntegerField()
    package_code = models.IntegerField()

    def __str__(self):
        return self.name



