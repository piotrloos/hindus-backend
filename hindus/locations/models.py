from django.db import models
from django.db.models.deletion import PROTECT


class City(models.Model):

    objects = models.Manager()

    order = models.PositiveIntegerField(default=0, unique=True)
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return "[{id}] {name}".format(id=self.pk, name=self.name)

    class Meta:
        verbose_name_plural = "cities"
        ordering = ['order']


class Trailer(models.Model):

    objects = models.Manager()

    order = models.PositiveIntegerField(default=0, unique=True)
    name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=PROTECT, related_name='trailers')
    open_hours_workday = models.CharField(max_length=32, blank=True)
    open_hours_saturday = models.CharField(max_length=32, blank=True)
    open_hours_sunday = models.CharField(max_length=32, blank=True)
    address = models.CharField(max_length=128, blank=True)
    telephone = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return "[{id}] {name}".format(id=self.pk, name=self.name)

    class Meta:
        verbose_name_plural = "trailers"
        ordering = ['order']


class Foodtruck(models.Model):

    objects = models.Manager()

    order = models.PositiveIntegerField(default=0, unique=True)
    name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=PROTECT, related_name='foodtrucks')
    open_hours_workday = models.CharField(max_length=32, blank=True)
    open_hours_saturday = models.CharField(max_length=32, blank=True)
    open_hours_sunday = models.CharField(max_length=32, blank=True)
    address = models.CharField(max_length=128, blank=True)
    telephone = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return "[{id}] {name}".format(id=self.pk, name=self.name)

    class Meta:
        verbose_name_plural = "foodtrucks"
        ordering = ['order']
