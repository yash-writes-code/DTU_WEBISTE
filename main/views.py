from django.shortcuts import render
from .models import Article
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    return render(request,"main/index.html")

def contact(request):
    return render(request,"main/contact.html")

def staff_details(request):
    return render(request,"main/staff.html")

def downloads(request,page):
    articles=Article.objects.all().order_by("-uploaded_at")
    paginator=Paginator(articles,8)
    page_object = paginator.get_page(page)
    context = {"page_obj": page_object}
    return render(request,"main/downloads.html",context=context)

def download_file(request, path):
    file_object=Article.objects.get(pk=path)
    response = HttpResponse(file_object.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{file_object.file.name}"'
    return response

def dashboard(request):
    return render(request,"main/dashboard.html")