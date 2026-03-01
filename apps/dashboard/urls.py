from django.urls import path
from apps.dashboard.views.home import dashboard_home
from apps.dashboard.views.portals import (
    admin_portal,
    teacher_portal,
    accountant_portal,
    receptionist_portal,
)

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_home, name='home'),
    path('admin/', admin_portal, name='admin_portal'),
    path('teacher/', teacher_portal, name='teacher_portal'),
    path('accountant/', accountant_portal, name='accountant_portal'),
    path('receptionist/', receptionist_portal, name='receptionist_portal'),
]