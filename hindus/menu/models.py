from django.db import models
from hindus.menu.choices import Spicy


class Dish(models.Model):
    name = models.CharField(max_length=64)
    order = models.IntegerField()
    spicy = models.IntegerField(default=1, choices=Spicy.CHOICES)
    description_pol = models.CharField(max_length=256, default="")
    description_eng = models.CharField(max_length=256, default="")
    picture_file = models.CharField(max_length=128)
    is_wege = models.BooleanField(default=False)
    is_cooked_today = models.BooleanField(default=False)

    def __str__(self):
        return self.__dict__.__str__()
