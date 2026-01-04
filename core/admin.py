from django.contrib import admin
from .models import Industry, City, Area, Address, Organization
from accounts.models import CustomerProfile, ProviderProfile

# Register your models here.
admin.site.register(Industry)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(Address)
admin.site.register(Organization)

admin.site.register(CustomerProfile)
admin.site.register(ProviderProfile)
