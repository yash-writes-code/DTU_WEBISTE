from django.urls import path
from .views import *

from django.shortcuts import redirect
app_name="main"
<<<<<<< HEAD:website/main/urls.py
=======

>>>>>>> 9ed7c20ed86faf17738664a45e3cee59583088cb:main/urls.py
urlpatterns=[
    path("",home,name="home"),
    path("downloads/",lambda request: redirect("1/"),name="downloads"),
    path("downloads/<int:page>/",downloads,name="downloads"),
    path("contact/",contact,name="contacts"),
    path("staff_enquiry/",staff_details,name="staff"),
    
    path("dashboard/",dashboard,name="dashboard"),
    path("download_file/<int:path>",download_file,name="download_file")
]