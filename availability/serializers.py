from rest_framework import serializers
from .models import OrganizationAvailability

class OrganizationAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationAvailability
        fields = (
            "id",
            "organization",
            "weekday",
            "start_time",
            "end_time",
            "is_active",
        )
                
    def validate(self, attrs):
        organization = attrs.get("organization")
        weekday = attrs.get("weekday")
        start_time = attrs.get("start_time")
        end_time = attrs.get("end_time")

        # time validation
        if start_time >= end_time:
            raise serializers.ValidationError(
                "start_time must be earlier than end_time."
            )

        # overlap validation
        overlapping_qs = OrganizationAvailability.objects.filter(
            organization=organization,
            weekday=weekday,
            is_active=True,
            start_time__lt=end_time,
            end_time__gt=start_time,
        )

        # for update case
        if self.instance:
            overlapping_qs = overlapping_qs.exclude(id=self.instance.id)

        if overlapping_qs.exists():
            raise serializers.ValidationError(
                "This availability overlaps with an existing time range."
            )

        return attrs
