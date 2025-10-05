from rest_framework import serializers
from .models import AvailabilitySlots

class AvailabilitySlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailabilitySlots
        fields = ["id", "name", "start_time", "end_time", "week_days", "is_available"]