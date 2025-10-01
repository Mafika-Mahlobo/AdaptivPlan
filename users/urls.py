from django.urls import path, include
from .views import RegisterView

urlpatterns = [
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api-auth/", include("rest_framework.urls")),
]