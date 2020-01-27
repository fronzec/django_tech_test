# coding: utf8
from django.urls import path

from .v1 import views as views_v1

# Urls V1 for locations endpoints
urlpatterns_v1_locations = ([path('', views_v1.LocationModelView.as_view()),
                             path('<str:pk>/', views_v1.LocationModelDetail.as_view()),
                             ], 'locations')

# Urls V1 for stations endpoints
urlpatterns_v1_stations = ([path('', views_v1.StationModelView.as_view()),
                            path('<str:pk>/', views_v1.StationModelDetail.as_view()),
                            ], 'stations')
