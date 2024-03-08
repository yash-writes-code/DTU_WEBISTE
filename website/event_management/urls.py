from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from .decorators import admin_required

app_name="event_management"
urlpatterns = [
    path("dashboard/",admin_required(dashboard),name="dashboard")
]
