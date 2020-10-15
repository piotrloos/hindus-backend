from django.db import models
from hindus.menu.choices import Spicy


class Dish(models.Model):

    name = models.CharField(max_length=64)
    order = models.IntegerField()
    spicy = models.IntegerField(default=1, choices=Spicy.CHOICES)
    description_pol = models.CharField(max_length=256, default="", null=True)
    description_eng = models.CharField(max_length=256, default="", null=True)
    picture_file = models.CharField(max_length=128, null=True)
    is_wege = models.BooleanField(default=False)
    is_cooked_today = models.BooleanField(default=False)

    def __str__(self):
        return "({id}) {name}".format(id=self.pk, name=self.name)
