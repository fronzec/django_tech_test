from .models import  LineModel, RouteModel

from rest_framework import generics

from .serializers import  LineModelSerializer, RouteModelSerializer


class LineModelList(generics.ListCreateAPIView):
    """
    API endpoint that allows list and creation operations for LineModel
    """
    queryset = LineModel.objects.all()
    serializer_class = LineModelSerializer


class RouteModelList(generics.ListCreateAPIView):
    """
    API endpoint that allows CRUD operations for RouteModel
    """
    queryset = RouteModel.objects.all()
    serializer_class = RouteModelSerializer


class RouteModelDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows RUD operations for RouteModel
    """
    queryset = RouteModel.objects.all()
    serializer_class = RouteModelSerializer


class LineModelDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows RUD operations for RouteModel
    """
    queryset = LineModel.objects.all()
    serializer_class = LineModelSerializer
