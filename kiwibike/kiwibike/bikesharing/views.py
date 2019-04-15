import citybikes
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Company, Location, Station
from .serializers import (CompanySerializer, LocationSerializer, StationSerializer, CompanyDetailSerializer,
                          NearbySerializer)

# Create your views here.

citybikes_client = citybikes.Client()


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
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("country", "city")

    def get_queryset(self):
        qs = Location.objects.all()
        qs = qs.prefetch_related("company")

        return qs


class StationListView(ListAPIView):
    serializer_class = StationSerializer
    queryset = Station.objects.all()

    def get_queryset(self):
        qs = Station.objects.all()
        qs = qs.prefetch_related("location", "location__company")

        return qs


class StationsNearbyView(APIView):

    def post(self, request):

        serializer = NearbySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        nearby = citybikes_client.networks.near(serializer.validated_data["lat"], serializer.validated_data["lon"])

        stations = []
        for station in nearby[:5]:
            data = station[0]
            d = {
                "name": data["company"],
                "lat": data["location"]["latitude"],
                "lon": data["location"]["longitude"],
                "dist": station[1]
            }
            stations.append(d)

        return Response(stations, status=200)
