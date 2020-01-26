# coding: utf8
from django.conf.urls import url
from django.urls import path

from .views import RouteModelList, RouteModelDetail, LineModelList, LineModelDetail

urlpatterns_routes = ([path('', RouteModelList.as_view()),
                       path('<str:pk>/', RouteModelDetail.as_view()),
                       ], 'routes')

urlpatterns_lines = ([path('', LineModelList.as_view()),
                      path('<str:pk>/', LineModelDetail.as_view()),
                      ], 'lines')
