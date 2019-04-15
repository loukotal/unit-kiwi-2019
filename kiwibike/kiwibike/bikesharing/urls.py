from django.urls import path, include  # noqa

from django.conf import settings
from .views import (CompanyListView, LocationListView, StationListView, StationsNearbyView, CompanyRetrieveView,
                    LocationCityListView)

urlpatterns = [
    path("companies/", CompanyListView.as_view()),
    path("companies/<str:name>/", CompanyRetrieveView.as_view()),
    path("locations/", LocationListView.as_view()),
    path("locations/<str:city>/", LocationCityListView.as_view()),
    path("stations/", StationListView.as_view()),
    path("nearby/", StationsNearbyView.as_view()),
]
