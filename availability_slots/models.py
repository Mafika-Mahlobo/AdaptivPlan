from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AvailabilitySlots(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    week_days = models.JSONField(default=list, blank=True)
    is_available = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="availability_slot")
