from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer