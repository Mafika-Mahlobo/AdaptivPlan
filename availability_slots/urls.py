from django.urls import include, path
from . import views
from tasks.views import TasksAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"availability_slots", views.AvailabilitySlotsAPIVew, basename="availability_slots")
router.register(r"tasks",TasksAPIView, basename="tasks" )

urlpatterns = [
    path("api/", include(router.urls)),
]