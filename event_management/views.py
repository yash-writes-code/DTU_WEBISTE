from django.shortcuts import render
from .models import Event
# Create your views here.
def home(request):
    obj=Event.objects.all()
    ctx={"Events":obj}
    return render(request,"event_management/index.html",ctx)
