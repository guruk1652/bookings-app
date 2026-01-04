from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import Area, City, Organization

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

    CUSTOMER = "CUSTOMER"
    PROVIDER = "PROVIDER"

    ROLE_CHOICES = (
        (CUSTOMER, "Customer"),
        (PROVIDER, "Provider"),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=CUSTOMER
    )



class CustomerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    area = models.ForeignKey(
        Area,
        on_delete=models.SET_NULL,
        null=True
    )

    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True
    )


class ProviderProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="providers"
    )
    is_active = models.BooleanField(default=True)