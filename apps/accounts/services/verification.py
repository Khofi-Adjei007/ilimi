import logging
from django.db import transaction
from apps.accounts.models import User, PhoneVerificationOTP

logger = logging.getLogger(__name__)


@transaction.atomic
def verify_phone_otp(user, code):
    """
    Verify a phone OTP code for a user.
    Returns (success: bool, message: str)
    """
    try:
        otp_record = PhoneVerificationOTP.objects.get(user=user)
    except PhoneVerificationOTP.DoesNotExist:
        return False, 'No verification code found. Please request a new one.'

    success, message = otp_record.verify(code)

    if success:
        user.is_phone_verified = True
        user.is_active = True
        user.save(update_fields=['is_phone_verified', 'is_active'])
        logger.info(f"Phone verified for user: {user.email}")

    return success, message