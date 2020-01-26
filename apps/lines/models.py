# coding: utf8
import uuid

from django.db import models

from apps.stations.models import StationModel


class LineModel(models.Model):
    """
    The line model

    Fields:
        name - the name of the line
        color - the color of the line
    """
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)


class RouteModel(models.Model):
    """
    The Route model, composed by a line 1-1 relation and many stations

    Fields:
        line - the associated line
        stations - the station of the route
        direction - True if has direction
        is_active - True if the route is active
    """
    line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(StationModel)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
