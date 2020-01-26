from rest_framework import serializers

from . import models


class LineModelSerializer(serializers.ModelSerializer):
    """
    Serializer for LineModel in list/detail endpoints
    """
    class Meta:
        model = models.LineModel
        fields = ('id', 'name', 'color')


class RouteModelSerializer(serializers.ModelSerializer):
    """
    Serializer for RouteModel in list/detail endpoints
    """
    class Meta:
        model = models.RouteModel
        fields = '__all__'
