from django.urls import path
from availability.views import OrganizationAvailabilityCreateAPIView

urlpatterns = [
    path("availability/", view=OrganizationAvailabilityCreateAPIView.as_view())
]