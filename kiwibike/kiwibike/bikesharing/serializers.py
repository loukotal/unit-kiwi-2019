from rest_framework import serializers

from .models import Company, Location, Station


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class LocationDetailSerializer(serializers.ModelSerializer):
    pass


class CompanyDetailSerializer(serializers.ModelSerializer):
    location_set = LocationSerializer(many=True)

    class Meta:
        model = Company
        fields = ("name", "location_set")


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = "__all__"
