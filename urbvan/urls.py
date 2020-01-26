# coding: utf8
from django.contrib import admin
from django.urls import (include, path)

from rest_framework.authtoken import views

from apps.stations.urls import urlpatterns_v1_locations, urlpatterns_v1_stations
from apps.lines.urls import urlpatterns_lines, urlpatterns_routes


# API endpoints
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    # TODO: 25/01/2020 refactor urls with a better structure
    path('v1/locations/', include(urlpatterns_v1_locations)),
    path('v1/stations/', include(urlpatterns_v1_stations)),
    path('v1/lines/', include(urlpatterns_lines)),
    path('v1/routes/', include(urlpatterns_routes))
]
