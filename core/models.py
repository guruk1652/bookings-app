from django.db import models
from django.db.models import UniqueConstraint

# Create your models here.

class Industry(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    is_standard = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class City(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("name",)


class Area(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        related_name="areas"
    )

    class Meta:
        unique_together = ("name", "city")


class Address(models.Model):
    address_line = models.TextField()
    area = models.ForeignKey(
        Area,
        on_delete=models.PROTECT
    )
    city = models.ForeignKey(
        City,
        on_delete=models.PROTECT
    )
    pincode = models.IntegerField(
        max_length=10
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    class Meta:
        indexes = [
            models.Index(fields=["area"]),
            models.Index(fields=["city"]),
        ]


class Organization(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    industry = models.ForeignKey(
        Industry,
        on_delete=models.PROTECT,
        related_name="organizations"
    )
    address = models.OneToOneField(
        Address,
        on_delete=models.PROTECT,
        related_name="organization"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = [
            models.Index(fields=["industry", "is_active"])
        ]

        constraints = [
            # Replaces unique_together
            UniqueConstraint(
                fields=['name', 'industry'], 
                name='unique_org_name_per_industry'
            )
        ]


    def __str__(self):
        return self.name
    

