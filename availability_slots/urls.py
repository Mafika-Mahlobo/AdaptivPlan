from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"availability_slots", views.AvailabilitySlotsAPIVew, basename="availability_slots")

urlpatterns = [
    path("api/", include(router.urls)),
]