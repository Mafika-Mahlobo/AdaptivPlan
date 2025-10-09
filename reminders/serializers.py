from rest_framework import serializers
from tasks.models import Task

class RemindersSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(source="slot.start_time", read_only=True)
    end_time = serializers.TimeField(source="slot.end_time", read_only=True)
    days_of_week = serializers.JSONField(source="slot.days_of_week", read_only=True)

    class Meta:
        model = Task
        fields = ["id", "title", "description", "start_time", "end_time", "days_of_week"]