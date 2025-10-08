from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from availability_slots.models import AvailabilitySlots

User = get_user_model()

class Task(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(AvailabilitySlots, 
                             on_delete=models.SET_NULL, 
                             null=True, blank=True, related_name="task")
    
    def clean(self):
        tasks = Task.objects.filter(user=self.user).exclude(id=self.id)

        for task in tasks:

            if not self.slot == None:
                if self.slot == task.slot:
                    raise ValidationError(f"Slot '{self.slot}' is already assigned to Task '{task.title}'")
            
            
    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)

            
            

