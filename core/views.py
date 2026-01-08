from django.core.cache import cache
from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Industry, Organization
from .serializers import IndustrySerializer, OrganizationSerializer
# Create your views here.
class IndustryListView(generics.ListAPIView):
    # queryset = Industry.objects.filter(is_standard=True)
    serializer_class = IndustrySerializer

    def get_queryset(self):
        cache_key = "industries:list"
        industries = cache.get(cache_key)

        if industries is None:
            industries = Industry.objects.filter(is_standard=True).order_by("name")
            cache.set(cache_key, industries, timeout= 60 * 60 * 24)
        
        return industries


class OrganizationListAPIView(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']

    def get_queryset(self):
        params = self.request.query_params
        industry_id = params.get("industry_id")
        area_id = params.get("area_id")
        city_id = params.get("city_id")

        if not industry_id:
            raise ValidationError(
                {
                    "industry_id": "This query parameter is required."
                }
            )
        
        if not industry_id.isdigit():
            raise ValidationError(
                {"industry_id": "Must be a valid integer."}
            )
        
        cache_key = (
            f"orgs:"
            f"industry={industry_id}:"
            f"area={params.get('area_id')}:"
            f"city={params.get('city_id')}:"
            f"search={params.get('search')}:"
            f"ordering={params.get('ordering')}"
        )

        queryset = cache.get(cache_key)

        if queryset is not None:
            return queryset

        queryset = Organization.objects.filter(
            industry_id=industry_id, is_active=True
                                               ).select_related(
                                                   "address", 
                                                   "address__area", 
                                                   "address__city"
                                                   )
        
        if area_id and area_id.isdigit():
            queryset = queryset.filter(address__area_id=area_id)

        elif city_id and city_id.isdigit():
            queryset = queryset.filter(address__city_id=city_id)
        
        queryset = queryset.order_by("name")
        
        cache.set(cache_key, queryset, timeout= 60 * 5)

        return queryset

        
