from rest_framework import serializers
from .models import Industry, Organization, Area, City


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['id', 'name']


class AreaMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'name']

class CityMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']

class OrganizationSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source="address.address_line", read_only=True)
    area = AreaMiniSerializer(source="address.area", read_only=True)
    city = CityMiniSerializer(source="address.city", read_only=True)
    class Meta:
        model = Organization
        fields = ['id', 'name', 'is_active', 'address', 'area', 'city']