from django.db import models
from .choices import Spicy


class Dish(models.Model):
    name = models.CharField(max_length=64)
    description_pol = models.CharField(max_length=256, default="")
    description_eng = models.CharField(max_length=256, default="")
    spicy = models.IntegerField(default=1, choices=Spicy.CHOICES)
    picture_url = models.CharField(max_length=128)
    is_cooked_today = models.BooleanField(default=False)
