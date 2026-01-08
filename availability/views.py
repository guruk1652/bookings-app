from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import OrganizationAvailability
from .serializers import OrganizationAvailabilitySerializer
from .permissions import IsProvider

# Create your views here.
class OrganizationAvailabilityCreateAPIView(CreateAPIView):
    serializer_class = OrganizationAvailabilitySerializer
    permission_classes = [IsProvider]

    def perform_create(self, serializer):
        organization = self.request.user.provider_profile.organization
        serializer.save(organization=organization)
