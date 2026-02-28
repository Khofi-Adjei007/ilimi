from django.urls import path
from apps.tenants.views import onboarding_branch, onboarding_complete

app_name = 'tenants'

urlpatterns = [
    path('onboarding/branch/', onboarding_branch, name='onboarding_branch'),
    path('onboarding/complete/', onboarding_complete, name='onboarding_complete'),
]