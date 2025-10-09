from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from availability_slots.permissions import IsOwner
from django.core.mail import send_mail
from .models import Task
from .serializers import TaskSerializer

class TasksAPIView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)

        send_mail(
            subject="Task creation success",
            message= f"Hi {self.request.user.email},\n You task '{task.title}' has been successfully cerated.",
            from_email='AdaptivPlan.gmail.com',
            recipient_list=[self.request.user.email],
            fail_silently=False
        )