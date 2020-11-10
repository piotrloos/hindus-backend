from django.db import models
from django.db.models.deletion import PROTECT
from django.utils.timezone import now
from hindus.dishes.models import Dish
from hindus.locations.models import Trailer, Foodtruck


class TrailerMenu(models.Model):

    objects = models.Manager()

    serving_date = models.DateField(default=now)
    trailer = models.ForeignKey(Trailer, on_delete=PROTECT, unique_for_date="serving_date", related_name='menu')
    dishes = models.ManyToManyField(Dish, blank=True, related_name='trailer_menu')

    def __str__(self):
        return "[{id}] {date} {trailer}".format(id=self.pk, date=self.serving_date, trailer=self.trailer)

    class Meta:
        verbose_name_plural = "trailer menus"
        ordering = ['serving_date', 'trailer']


class FoodtruckMenu(models.Model):

    objects = models.Manager()

    serving_date = models.DateField(default=now)
    foodtruck = models.ForeignKey(Foodtruck, on_delete=PROTECT, unique_for_date="serving_date", related_name='menu')
    dishes = models.ManyToManyField(Dish, blank=True, related_name='foodtruck_menu')

    def __str__(self):
        return "[{id}] {date} {foodtruck}".format(id=self.pk, date=self.serving_date, foodtruck=self.foodtruck)

    class Meta:
        verbose_name_plural = "foodtruck menus"
        ordering = ['serving_date', 'foodtruck']
