"""
Availability slots View.

- It allows CRUD operation on Availability slots
"""

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .models import AvailabilitySlots
from .serializers import AvailabilitySlotsSerializer

class AvailabilitySlotsAPIVew(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = AvailabilitySlotsSerializer

    def get_queryset(self):
        return AvailabilitySlots.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
   