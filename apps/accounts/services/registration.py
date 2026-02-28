import logging
from django.db import transaction
from django.utils import timezone
from datetime import timedelta
from apps.accounts.models import User, PhoneVerificationOTP
from apps.notifications.services.sms import send_otp_sms

logger = logging.getLogger(__name__)


@transaction.atomic
def create_user_account(step1_data):
    """
    Create a new user account from step 1 registration data.
    User is inactive until phone is verified.
    Returns (user, otp) tuple.
    """
    user = User.objects.create_user(
        email=step1_data['email'],
        password=step1_data['password1'],
        first_name=step1_data['first_name'],
        last_name=step1_data['last_name'],
        phone_number=step1_data['phone_number'],
        is_active=False,
    )

    otp = PhoneVerificationOTP.create_for_user(user)
    send_otp_sms(user.phone_number, otp.otp)

    logger.info(f"New user account created: {user.email}")
    return user, otp


def resend_otp(user):
    """
    Resend OTP to user's phone number.
    Rate limited — can only resend once per minute.
    Returns (success, message)
    """
    existing = PhoneVerificationOTP.objects.filter(user=user).first()

    if existing:
        time_since_creation = timezone.now() - existing.created_at
        if time_since_creation < timedelta(minutes=1):
            seconds_left = 60 - int(time_since_creation.total_seconds())
            return False, f'Please wait {seconds_left} seconds before requesting a new code.'

    otp = PhoneVerificationOTP.create_for_user(user)
    send_otp_sms(user.phone_number, otp.otp)
    return True, 'A new verification code has been sent to your phone.'