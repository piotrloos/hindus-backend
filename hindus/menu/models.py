from django.db import models
from django.db.models.deletion import PROTECT
from datetime import date
from hindus.menu.choices import Spicy
from hindus.locations.models import Location


class Dish(models.Model):

    order = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length=64)
    spicy = models.IntegerField(default=1, choices=Spicy.CHOICES)
    description_pol = models.CharField(max_length=256, default="")
    description_eng = models.CharField(max_length=256, default="")
    picture_file = models.CharField(max_length=128)
    is_vegetarian = models.BooleanField(default=False)
    is_cooked_today = models.BooleanField(default=False)

    def __str__(self):
        return "({id}) {name}".format(id=self.pk, name=self.name)

    class Meta:
        verbose_name_plural = "Dishes"


class DailyMenu(models.Model):

    serving_date = models.DateField(default=date.today)
    location = models.ForeignKey(Location, on_delete=PROTECT, unique_for_date="serving_date")
    dishes = models.ManyToManyField(Dish)

    def __str__(self):
        return "({id}) {date} {location}".format(id=self.pk, date=self.serving_date, location=self.location)

    class Meta:
        verbose_name_plural = "Daily Menu"
