from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from availability_slots.permissions import IsOwner
from .serializers import RemindersSerializer
from tasks.models import Task
from django.utils import timezone

class RemindersAPIView(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = RemindersSerializer

    def get_queryset(self):
        user = self.request.user
        now = timezone.localtime(timezone.now()).time()
        today = timezone.localtime(timezone.now()).isoweekday()
        
        tasks = (
            Task.objects.filter(user=user, slot__isnull=False).
            select_related("slot").order_by("slot__start_time")
        )

        upcomming_tasks = []
        for task in tasks:
            if task.slot.start_time >= now and today in (task.slot.week_days or []):
                upcomming_tasks.append(task)

        return upcomming_tasks

