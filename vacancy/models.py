from django.db import models


class Vacancy(models.Model):
    title = models.TextField()
    salary = models.IntegerField()

    def __str__(self):
        return self.title



