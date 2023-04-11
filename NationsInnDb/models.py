from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Nation(models.Model):
    id = models.IntegerField()

    name = models.CharField(
        max_length=160, primary_key=True)

    description = models.TextField()

    facebook_Link = models.CharField(max_length=160, null=True, blank=True)

    site_Link = models.CharField(max_length=160, null=True, blank=True)

    latitude = models.DecimalField(
        max_digits=8, decimal_places=5, null=True, blank=True)

    longitude = models.DecimalField(
        max_digits=8, decimal_places=5, null=True, blank=True)

    address = models.CharField(max_length=160, null=True, blank=True)

    logo = models.CharField(max_length=160, null=True,
                            blank=True)

    marker = models.CharField(max_length=160, null=True, blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):

    title = models.CharField(max_length=160, unique=False)

    starttime = models.DateTimeField(null=True, blank=True)

    endtime = models.DateTimeField(null=True, blank=True)

    nation = models.ForeignKey(
        Nation, on_delete=models.CASCADE, default=None, null=True, blank=True)

    location = models.CharField(max_length=160, null=True, blank=True)

    link = models.CharField(max_length=160, null=True, blank=True)

    description = models.TextField()

    logo = models.CharField(max_length=160, null=True, blank=True)

    def __str__(self):
        return self.title
