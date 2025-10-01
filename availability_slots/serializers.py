from rest_framework import serializers
from .models import AvailabilitySlots

class AvailabilitySlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailabilitySlots
        fields = "__all__"