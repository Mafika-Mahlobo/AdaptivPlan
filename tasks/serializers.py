"""
Task serializer.
"""

from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError
from .models import Task
from availability_slots.models import AvailabilitySlots

class TaskSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        """
        init override. Filters availability slots by current user.
        """

        super().__init__(*args, **kwargs)
        request = self.context.get("request") 
        if request and hasattr(request, "user"):
            self.fields["slot"].queryset = AvailabilitySlots.objects.filter(user=request.user)

    class Meta:
        model = Task
        fields = ["id", "title", "description", "slot"]

    def validate_title(self, value):
        """
        Capitilizes and strip task title for comparison.
        """
        value = value.strip()
        return value.capitalize()

    def validate(self, attrs):
        """
        validate override. Ensures that users cannot view or edit another user's tasks.
        """

        user = self.context["request"].user
        instance = Task(**attrs, user=user)

        try:
            instance.clean()

        except DjangoValidationError as e:
            raise serializers.ValidationError({"non_field_errors": e.messages})
        
        return attrs