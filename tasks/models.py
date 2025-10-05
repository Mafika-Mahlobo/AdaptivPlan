from django.db import models
from django.contrib.auth import get_user_model
from availability_slots.models import AvailabilitySlots

User = get_user_model()

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(AvailabilitySlots, 
                             on_delete=models.SET_NULL, 
                             null=True, blank=True, related_name="task")
