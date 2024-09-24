from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    is_deleted = models.BooleanField(default=False, editable=False)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
