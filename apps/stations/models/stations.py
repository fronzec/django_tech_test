# coding: utf8
import uuid

from django.db import models

from .locations import LocationModel


class StationModel(models.Model):
    """ It represents a station

        Fields:
            location -- The location for the current location.
            order -- The order number for the current station.
            is_active -- True if the station is active, otherwise False
    """
    location = models.ForeignKey(LocationModel, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
