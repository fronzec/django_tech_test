# coding: utf8
from rest_framework import generics

from urbvan_framework.views import ListCreateView
from .schemas import LocationSchema, StationSchema
from .serializers import LocationSerializer, StationModelSerializer
from ..models import LocationModel, StationModel


class LocationModelView(ListCreateView):

    queryset = LocationModel.objects.all()
    # TODO: 24/01/20 revies is schema or schema_class
    schema_class = LocationSchema
    serializer_class = LocationSerializer


class LocationModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocationModel.objects.all()
    serializer_class = LocationSerializer


class StationModelView(ListCreateView):
    queryset = StationModel.objects.all()
    schema_class = StationSchema
    serializer_class = StationModelSerializer


class StationModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StationModel.objects.all()
    serializer_class = StationModelSerializer
