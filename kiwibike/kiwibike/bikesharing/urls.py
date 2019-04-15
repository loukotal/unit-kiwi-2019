from django.urls import path, include  # noqa

from django.conf import settings
from .views import (CompanyListView, LocationListView, StationListView, StationsNearbyView, CompanyRetrieveView,
                    LocationCityListView, StationsNearbyAirportView, GetRoute)

urlpatterns = [
    path("companies/", CompanyListView.as_view()),
    path("companies/<int:pk>/", CompanyRetrieveView.as_view()),
    path("locations/", LocationCityListView.as_view()),
    path("stations/", StationListView.as_view()),
    path("nearby/", StationsNearbyView.as_view()),
    path("airport-nearby/", StationsNearbyAirportView.as_view()),
    path("get-route/", GetRoute.as_view()),
]
