from django.db import models
from django.db.models import ForeignKey, CASCADE

from account.models import Account


class Post(models.Model):
    body = models.TextField()
    author = ForeignKey(Account, CASCADE, 'posts')





