from django.urls import path
from .views import lawyer_dashboard, user_dashboard

urlpatterns = [

    path("lawyer/", lawyer_dashboard, name="lawyer_dashboard"),

    path("user/", user_dashboard, name="user_dashboard"),

]