# coding: utf8
import uuid

from django.db import models

from .locations import LocationModel


class StationModel(models.Model):
    """ It represents a station

        Fields:
            id -- The unique identifier, see app.utils.create_id function
            location -- The location for the current location.
            order -- The order number for the current station.
            is_active -- True if the station is active, otherwise False
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.ForeignKey(LocationModel, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
