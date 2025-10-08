from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError
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

    def validate_title(self, value):
        value = value.strip()
        return value.capitalize()

    def validate(self, attrs):

        user = self.context["request"].user
        instance = Task(**attrs, user=user)

        try:
            instance.clean()

        except DjangoValidationError as e:
            raise serializers.ValidationError({"non_field_errors": e.messages})
        
        return attrs