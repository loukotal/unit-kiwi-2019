from rest_framework import serializers

from .models import Company, Location, Station


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Location
        fields = "__all__"


class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("lat", "lon", "city", "country")


class CompanyDetailSerializer(serializers.ModelSerializer):
    location_set = LocationDetailSerializer(many=True)

    class Meta:
        model = Company
        fields = ("name", "location_set")


class StationSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = Station
        fields = "__all__"


class NearbySerializer(serializers.Serializer):
    lat = serializers.FloatField(required=True)
    lon = serializers.FloatField(required=True)