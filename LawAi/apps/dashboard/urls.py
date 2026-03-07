from django.urls import path
from .views import lawyer_dashboard

urlpatterns = [

    path("lawyer/", lawyer_dashboard, name="lawyer_dashboard")

]