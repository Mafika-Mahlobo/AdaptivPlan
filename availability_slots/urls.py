from django.urls import include, path
from . import views
from tasks.views import TasksAPIView
from reminders.views import RemindersAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"availability_slots", views.AvailabilitySlotsAPIVew, basename="availability_slots")
router.register(r"tasks",TasksAPIView, basename="tasks" )
router.register(r"reminders", RemindersAPIView, basename="reminders")

urlpatterns = [
    path("api/", include(router.urls)),
]