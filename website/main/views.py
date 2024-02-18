from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"main/index.html")

def contact(request):
    return render(request,"main/contact.html")

def staff_details(request):
    return render(request,"main/staff.html")

def downloads(request):
    return render(request,"main/downloads.html")