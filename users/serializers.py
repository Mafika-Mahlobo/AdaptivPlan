"""
User serializer.
"""

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}) # Hide password when typing

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "password", "time_zone"]


    def create(self, validated_data):
        """
        Validate user and hash password before saving.
        """
        user = User.objects.create_user(**validated_data)
        return user

    