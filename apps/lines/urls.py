# coding: utf8
from django.urls import path

from .views import RouteModelList, RouteModelDetail, LineModelList, LineModelDetail

# Url patters for routes
urlpatterns_routes = ([path('', RouteModelList.as_view()),
                       path('<str:pk>/', RouteModelDetail.as_view()),
                       ], 'routes')

# Url patters for lines
urlpatterns_lines = ([path('', LineModelList.as_view()),
                      path('<str:pk>/', LineModelDetail.as_view()),
                      ], 'lines')
