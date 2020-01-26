# coding: utf8
import factory

from .models import LocationModel


class LocationFactory(factory.django.DjangoModelFactory):
    """
    Location factory for unit test
    """
    class Meta:
        model = LocationModel

    name = factory.Faker('slug')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')
