from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import Industry, Organization
from .serializers import IndustrySerializer, OrganizationSerializer
# Create your views here.
class IndustryListView(generics.ListAPIView):
    queryset = Industry.objects.filter(is_standard=True)
    serializer_class = IndustrySerializer


class OrganizationListAPIView(generics.ListAPIView):
    serializer_class = OrganizationSerializer

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

        queryset = Organization.objects.filter(
            industry_id=industry_id, is_active=True
                                               ).select_related(
                                                   "address", 
                                                   "address__area", 
                                                   "address__city"
                                                   )
        
        if area_id:
            queryset = queryset.filter(address__area_id=area_id)
        if city_id:
            queryset = queryset.filter(address__city_id=city_id)
        
        return queryset.order_by("name")

        
