import citybikes
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Company, Location, Station
from .serializers import (CompanySerializer, LocationSerializer, StationSerializer, CompanyDetailSerializer,
                          NearbySerializer)

from .utils import airport_coordinates, mapbox, get_poi
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


class StationsNearbyAirportView(APIView):

    def post(self, request):



        airport_code = request.data.get("airport_code")
        data = airport_coordinates("id", airport_code)
        nearby = citybikes_client.networks.near(data["lat"], data["lon"])

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


class GetRoute(APIView):

    def post(self, request):
        data = request.data

        lat_a, lon_a = data["lat_a"], data["lon_a"]
        lat_b, lon_b = data["lat_b"], data["lon_b"]

        map_data = mapbox((lat_a, lon_a,), (lat_b, lon_b)).geojson

        radius = data.get("raidus", "1000")
        limit = data.get("limit", 5)

        poi = get_poi(map_data, radius, limit)
        pata_list = []
        for point in poi:
            p = point.split("\n")
            pata = {
                "lat": float(p[1]),
                "lon": float(p[0]),
                "name": p[2],
                "category": p[3]
            }
            pata_list.append(pata)

        d = {
            "points_of_interest": pata_list,
            "route": list(map_data)
        }

        return Response(d, status=200)
