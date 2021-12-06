from django.db import models
from django.conf import settings

# Create your models here.


class Contributors(models.Model):
    user = models.ForeignKey()
    project = models.ForeignKey()


class Projects(models.Model):
    title = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )