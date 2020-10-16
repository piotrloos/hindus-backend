from django.db import models
from django.db.models import PROTECT


class City(models.Model):

    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return "({id}) {name}".format(id=self.pk, name=self.name)

    class Meta:
        verbose_name_plural = "Cities"


class Location(models.Model):

    order = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=PROTECT, null=True)
    opening_hours_workday = models.CharField(max_length=32)
    opening_hours_saturday = models.CharField(max_length=32)
    opening_hours_sunday = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    telephone = models.IntegerField(null=True)

    def __str__(self):
        return "({id}) {name}".format(id=self.pk, name=self.name)

    class Meta:
        verbose_name_plural = "Locations"
