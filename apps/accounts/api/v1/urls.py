from django.urls import path
from .views import (
    RegisterStep1View,
    RegisterStep2View,
    OTPVerifyView,
    OTPResendView,
    IlimiTokenObtainView,
    IlimiTokenRefreshView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
)

app_name = "auth-v1"

urlpatterns = [
    path("register/step1/", RegisterStep1View.as_view(), name="register-step1"),
    path("register/step2/", RegisterStep2View.as_view(), name="register-step2"),
    path("verify/otp/", OTPVerifyView.as_view(), name="otp-verify"),
    path("verify/otp/resend/", OTPResendView.as_view(), name="otp-resend"),
    path("token/", IlimiTokenObtainView.as_view(), name="token-obtain"),
    path("token/refresh/", IlimiTokenRefreshView.as_view(), name="token-refresh"),
    path("password/reset/", PasswordResetRequestView.as_view(), name="password-reset"),
    path("password/reset/confirm/", PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
]