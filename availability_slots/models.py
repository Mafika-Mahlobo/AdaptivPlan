"""
Availability slots model.
"""

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class AvailabilitySlots(models.Model):
    """
    Model attributes definition.
    """

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



    def clean(self):
        """
        Clean method override for availability slot POST and PUT validations.
        """

        slots = AvailabilitySlots.objects.filter(user=self.user).exclude(id=self.id)

        if self.start_time == self.end_time:
            raise ValidationError("Start time and end time cannot be the same")
        
        if self.start_time >= self.end_time:
            raise ValidationError("End time cannot be earlier than start time.")
        
        for slot in slots:
            if set(self.week_days).intersection(set(slot.week_days)):
                if self.start_time == slot.start_time and self.end_time == slot.end_time:
                    raise ValidationError(
                        f"Duplicate detected with slot '{slot.name}'. You start and end time cannot be the same on the same days"
                        )
                if self.start_time < slot.end_time and self.end_time > slot.start_time:
                    raise ValidationError(
                        f"Slot '{self.name}' overlaps with '{slot.name}' on shared days"
                        )
                
    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"
