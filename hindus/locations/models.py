from django.db import models
from django.db.models.deletion import PROTECT
from hindus.menu.models import Dish
from datetime import date


class City(models.Model):

    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return "[{id}] {name}".format(id=self.pk, name=self.name)

    class Meta:
        verbose_name_plural = "Cities"


class Location(models.Model):

    order = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=PROTECT, related_name='locations')
    opening_hours_workday = models.CharField(max_length=32, blank=True)
    opening_hours_saturday = models.CharField(max_length=32, blank=True)
    opening_hours_sunday = models.CharField(max_length=32, blank=True)
    address = models.CharField(max_length=128, blank=True)
    telephone = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return "[{id}] {name}".format(id=self.pk, name=self.name)

    class Meta:
        verbose_name_plural = "Locations"


class DailyMenu(models.Model):

    serving_date = models.DateField(default=date.today)
    location = models.ForeignKey(Location, on_delete=PROTECT, unique_for_date="serving_date", related_name='menu')
    dishes = models.ManyToManyField(Dish, blank=True, related_name='dailymenu')

    def __str__(self):
        return "[{id}] {date} {location}".format(id=self.pk, date=self.serving_date, location=self.location)

    class Meta:
        verbose_name_plural = "Daily Menu"
