"""
Ilimi Central API Router
All versioned API endpoints are registered here.
"""

from django.urls import path, include

urlpatterns = [
    path("v1/auth/", include("apps.accounts.api.v1.urls", namespace="auth-v1")),
    path("v1/schools/", include("apps.tenants.api.v1.urls", namespace="tenants-v1")),
]