from django.db import models
from django.db.models import SET_NULL


class City(models.Model):

    name = models.CharField(max_length=32)

    def __str__(self):
        return "({id}) {name}".format(id=self.pk, name=self.name)


class Location(models.Model):

    order = models.IntegerField()
    name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=SET_NULL, null=True)
    opening_hours_workday = models.CharField(max_length=32, null=True)
    opening_hours_saturday = models.CharField(max_length=32, null=True)
    opening_hours_sunday = models.CharField(max_length=32, null=True)
    address = models.CharField(max_length=128, null=True)
    telephone = models.IntegerField(null=True)

    def __str__(self):
        return "({id}) {name}".format(id=self.pk, name=self.name)
