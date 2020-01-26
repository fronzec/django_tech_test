# coding: utf8
from rest_framework import serializers

from apps.stations.models import LocationModel, StationModel


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationModel
        exclude = ('id', )


class LocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = '__all__'


class StationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationModel
        fields = '__all__'
