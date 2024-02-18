from django.urls import path
from .views import *

urlpatterns=[
    path("",home,name="home"),
    path("downloads/",downloads),
    path("contact/",contact),
    path("gastaff/",staff_details),

]