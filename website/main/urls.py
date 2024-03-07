from django.urls import path
from .views import *

from django.shortcuts import redirect

urlpatterns=[
    path("",home,name="home"),
    path("downloads/",lambda request: redirect("1/")),
    path("downloads/<int:page>/",downloads,name="downloads"),
    path("contact/",contact),
    path("gastaff/",staff_details),
    path("dashboard/",dashboard),
    path("download_file/<int:path>",download_file,name="download_file"),
    
]