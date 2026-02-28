from django.urls import path
from apps.accounts.views import (
    login_view,
    logout_view,
    password_reset_request,
    set_new_password,
)

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('password-reset/', password_reset_request, name='password_reset'),
    path('password-reset/<str:token>/', set_new_password, name='set_new_password'),
]