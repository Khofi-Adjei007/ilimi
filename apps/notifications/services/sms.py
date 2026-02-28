from django.conf import settings
from django.utils.module_loading import import_string
import logging

logger = logging.getLogger(__name__)


def get_sms_backend():
    backend_path = getattr(settings, 'SMS_BACKEND', 'apps.notifications.backends.console.ConsoleSMSBackend')
    backend_class = import_string(backend_path)
    return backend_class()


def send_sms(recipient, message, sender_id=None):
    """
    Send an SMS message using the configured backend.
    Returns dict with status and any relevant data.
    """
    backend = get_sms_backend()
    return backend.send(recipient, message, sender_id)


def send_otp_sms(recipient, otp_code):
    """Send OTP verification code via SMS."""
    message = (
        f"Your Ilimi verification code is: {otp_code}\n"
        f"This code expires in 10 minutes. Do not share it with anyone."
    )
    return send_sms(recipient, message)


def send_welcome_sms(recipient, school_name):
    """Send welcome SMS after successful onboarding."""
    message = (
        f"Welcome to Ilimi! Your school '{school_name}' has been successfully set up. "
        f"Your 30-day free trial has started. Visit ilimi.app to get started."
    )
    return send_sms(recipient, message)