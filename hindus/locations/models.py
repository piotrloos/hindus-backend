from django.db import models
from django.db.models.deletion import PROTECT


class City(models.Model):

    objects = models.Manager()

    order = models.PositiveIntegerField(
        default=0,
        unique=True,
        verbose_name="kolejność sortowania",
    )
    name = models.CharField(
        max_length=32,
        unique=True,
        verbose_name="nazwa miasta",
    )

    def __str__(self):
        return "[{id}] {name}".format(
            id=self.pk,
            name=self.name,
        )

    class Meta:
        verbose_name = "miasto"
        verbose_name_plural = "miasta"
        ordering = ['order']


class Trailer(models.Model):

    objects = models.Manager()

    order = models.PositiveIntegerField(
        default=0,
        unique=True,
        verbose_name="kolejność sortowania",
    )
    name = models.CharField(
        max_length=64,
        verbose_name="nazwa przyczepy",
    )
    city = models.ForeignKey(
        City,
        on_delete=PROTECT,
        related_name='trailers',
        verbose_name="miasto",
    )
    open_hours_workday = models.CharField(
        max_length=32,
        blank=True,
        verbose_name="godziny otwarcia pn-pt",
    )
    open_hours_saturday = models.CharField(
        max_length=32,
        blank=True,
        verbose_name="godziny otwarcia sb",
    )
    open_hours_sunday = models.CharField(
        max_length=32,
        blank=True,
        verbose_name="godziny otwarcia nd",
    )
    address = models.CharField(
        max_length=128,
        blank=True,
        verbose_name="adres przyczepy",
    )
    telephone = models.CharField(
        max_length=16,
        blank=True,
        verbose_name="telefon przyczepy",
    )

    def __str__(self):
        return "[{id}] {name}".format(
            id=self.pk,
            name=self.name,
        )

    class Meta:
        verbose_name = "przyczepa"
        verbose_name_plural = "przyczepy"
        ordering = ['order']


class Foodtruck(models.Model):

    objects = models.Manager()

    order = models.PositiveIntegerField(
        default=0,
        unique=True,
        verbose_name="kolejność sortowania",
    )
    name = models.CharField(
        max_length=64,
        verbose_name="nazwa foodtrucka",
    )
    city = models.ForeignKey(
        City,
        on_delete=PROTECT,
        related_name='foodtrucks',
        verbose_name="miasto",
    )
    open_hours_workday = models.CharField(
        max_length=32,
        blank=True,
        verbose_name="godziny otwarcia pn-pt",
    )
    open_hours_saturday = models.CharField(
        max_length=32,
        blank=True,
        verbose_name="godziny otwarcia sb",
    )
    open_hours_sunday = models.CharField(
        max_length=32,
        blank=True,
        verbose_name="godziny otwarcia nd",
    )
    address = models.CharField(
        max_length=128,
        blank=True,
        verbose_name="adres foodtrucka",
    )
    telephone = models.CharField(
        max_length=16,
        blank=True,
        verbose_name="telefon foodtrucka",
    )

    def __str__(self):
        return "[{id}] {name}".format(
            id=self.pk,
            name=self.name,
        )

    class Meta:
        verbose_name = "foodtruck"
        verbose_name_plural = "foodtrucki"
        ordering = ['order']
