from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import AvailabilitySlots
from .serializers import AvailabilitySlotsSerializer

class AvailabilitySlotsAPIVew(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AvailabilitySlotsSerializer

    def get_queryset(self):
        return AvailabilitySlots.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
   