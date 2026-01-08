from rest_framework.permissions import BasePermission

class IsProvider(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, "provider_profile") and
            request.user.provider_profile.is_active
        )
