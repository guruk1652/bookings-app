from django.shortcuts import render
from rest_framework import generics
from .models import Industry
from .serializers import IndustrySerializer

# Create your views here.
class IndustryListView(generics.ListAPIView):
    queryset = Industry.objects.filter(is_standard=True)
    serializer_class = IndustrySerializer
