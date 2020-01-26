from rest_framework import serializers

from . import models


class LineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LineModel
        fields = ('id', 'name', 'color')


class RouteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RouteModel
        fields = '__all__'
