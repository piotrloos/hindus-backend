from django.db import models
from django.db.models.deletion import PROTECT


class City(models.Model):

    objects = models.Manager()

    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return "[{id}] {name}".format(id=self.pk, name=self.name)

    class Meta:
        verbose_name_plural = "Cities"


class Trailer(models.Model):

    objects = models.Manager()

    order = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=PROTECT, related_name='trailers')
    opening_hours_workday = models.CharField(max_length=32, blank=True)
    opening_hours_saturday = models.CharField(max_length=32, blank=True)
    opening_hours_sunday = models.CharField(max_length=32, blank=True)
    address = models.CharField(max_length=128, blank=True)
    telephone = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return "[{id}] {name}".format(id=self.pk, name=self.name)

    class Meta:
        verbose_name_plural = "Trailers"


class Foodtruck(models.Model):

    objects = models.Manager()

    order = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=PROTECT, related_name='foodtrucks')
    opening_hours_workday = models.CharField(max_length=32, blank=True)
    opening_hours_saturday = models.CharField(max_length=32, blank=True)
    opening_hours_sunday = models.CharField(max_length=32, blank=True)
    address = models.CharField(max_length=128, blank=True)
    telephone = models.CharField(max_length=16, blank=True)

    def __str__(self):
        return "[{id}] {name}".format(id=self.pk, name=self.name)

    class Meta:
        verbose_name_plural = "Foodtrucks"
