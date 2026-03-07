from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/signing/", include("apps.signing.urls")),
    path("api/dashboard/", include("apps.dashboard.urls")),
]
