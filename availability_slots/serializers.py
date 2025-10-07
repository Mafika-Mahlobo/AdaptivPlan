from rest_framework import serializers
from .models import AvailabilitySlots
from django.core.exceptions import ValidationError as DjangoValidationError

class AvailabilitySlotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AvailabilitySlots
        fields = ["id", "name", "start_time", "end_time", "week_days", "is_available"]

    def validate(self, attrs):
        user = self.context["request"].user
        instance = AvailabilitySlots(**attrs, user=user)

        try:
            instance.clean()

        except DjangoValidationError as e:
            raise serializers.ValidationError({"non_field_errors": e.messages})
        
        return attrs