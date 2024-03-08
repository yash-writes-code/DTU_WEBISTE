# event_management/decorators.py
from functools import wraps
from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
    """
    Custom decorator to check if the user is an admin.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff and u.is_superuser,
        login_url='/admin/login/'
    )
    return actual_decorator(view_func)
