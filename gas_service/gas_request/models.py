from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class GasServiceRequest(models.Model):
    CATEGORY_CHOICES = (
        ('New Connection', 'New Connection'),
        ('Cylinder_Booking', 'Cylinder Booking'),
        ('Change_Address', 'Change Address'),
        ('Cylinder_Delivery', 'Cylinder Delivery'),
    )
    user = models.ForeignKey(User, models.CASCADE, default=None, null=True)
    customer_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    address = models.TextField()
    request_type = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)
    completion_timestamp = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f"Service Request from {self.customer_name} for {self.request_type}"
