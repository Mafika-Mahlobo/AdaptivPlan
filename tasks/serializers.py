from rest_framework import serializers
from .models import Task
from availability_slots.models import AvailabilitySlots

class TaskSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request") 
        if request and hasattr(request, "user"):
            self.fields["slot"].queryset = AvailabilitySlots.objects.filter(user=request.user)

    class Meta:
        model = Task
        fields = ["id", "title", "description", "slot"]