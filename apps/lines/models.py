# coding: utf8
import uuid

from django.db import models

from apps.stations.models import StationModel


class LineModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)


class RouteModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(StationModel)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
