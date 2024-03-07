from django.contrib import admin
from django.urls import path,reverse
from .models import *

from django.shortcuts import render
from django.utils.html import format_html
from django.http import HttpResponseRedirect


class EventAdmin(admin.ModelAdmin):
    change_list_template = "admin/event_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_site.admin_view(self.dashboard_view),name="dashboard_view"),
        ]
        return custom_urls + urls
    
    
    def dashboard_view(self, request,*args, **kwargs):
        # Your custom view logic for the dashboard
        url = reverse('event_management:dashboard')  # Use the correct view name here
        return HttpResponseRedirect(url)
      


admin.site.register(Event, EventAdmin)


admin.site.register(MenuItem)