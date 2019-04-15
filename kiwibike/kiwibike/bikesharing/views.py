import citybikes
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Company, Location, Station
from .serializers import CompanySerializer, LocationSerializer, StationSerializer, CompanyDetailSerializer


# Create your views here.


class CompanyListView(ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyRetrieveView(RetrieveAPIView):
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()


class LocationListView(ListAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationCityListView(ListAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    lookup_field = "city"


class StationListView(ListAPIView):
    serializer_class = StationSerializer
    queryset = Station.objects.all()


class StationsNearbyView(APIView):

    # TODO: Use citybikes API to return stations nearby
    def post(self, request):
        # TODO: Get all companies / locations from the request
        # TODO: Check for the nearest stations
        pass
