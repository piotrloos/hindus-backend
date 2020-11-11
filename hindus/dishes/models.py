from django.db import models
from hindus.dishes.choices import Spicy


class Dish(models.Model):

    objects = models.Manager()

    order = models.PositiveIntegerField(
        default=0,
        unique=True,
        verbose_name="kolejność sortowania",
    )
    name = models.CharField(
        max_length=64,
        verbose_name="nazwa dania",
    )
    spicy = models.IntegerField(
        default=1,
        choices=Spicy.CHOICES,
        verbose_name="ostrość",
    )
    description_pol = models.CharField(
        max_length=256,
        default="",
        verbose_name="opis polski",
    )
    description_eng = models.CharField(
        max_length=256,
        default="",
        verbose_name="opis angielski",
    )
    picture_file = models.CharField(
        max_length=128,
        verbose_name="nazwa pliku obrazka",
    )
    is_vegetarian = models.BooleanField(
        default=False,
        verbose_name="czy wege?",
    )

    def __str__(self):
        return "[{id}] {name}".format(
            id=self.pk,
            name=self.name,
        )

    class Meta:
        verbose_name = "danie"
        verbose_name_plural = "dania"
        ordering = ['order']
