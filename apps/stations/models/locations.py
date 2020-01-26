# coding: utf8
import uuid

from django.db import models


class LocationModel(models.Model):
    """ Location object is the representation of physical station

        Fields:
            id -- This is the unique identifier for object instance.
            name -- This is the common identifier for a physical location.
            coordinates --  Latitude and Longuitude as string.
                            example. "19.4094937,-99.1634261"
            geometry -- Similar to coordinate but using with postgis
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)

    def __str__(self):
        return self.name
