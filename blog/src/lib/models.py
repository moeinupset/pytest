from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_time = models.DateTimeField(
        auto_now_add=True, verbose_name='created time')
    modified_time = models.DateTimeField(
        auto_now=True, verbose_name='modified time')

    class Meta:
        abstract = True
