from django.urls import path, include
from .views import RegisterView, api_root

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("api-auth/", include("rest_framework.urls")),

    #Dummy view
    path("/api/", api_root, name="api_root"),
]