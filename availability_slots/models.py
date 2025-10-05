from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AvailabilitySlots(models.Model):
    SLOT_CHICES = [
        ("office", "Work / Office"),
        ("remote", "Work from home"),
        ("study", "Study"),
        ("break", "Free Time"),
        ("meeting", "Meeting"),
        ("travel", "Travel")
    ]
    name = models.CharField(max_length=100, choices=SLOT_CHICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    week_days = models.JSONField(default=list, blank=True)
    is_available = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="availability_slot")

    def __str__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"
