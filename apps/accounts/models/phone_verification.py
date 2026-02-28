import random
from django.db import models
from django.utils import timezone
from datetime import timedelta


def generate_otp():
    return str(random.randint(100000, 999999))


def otp_expiry():
    return timezone.now() + timedelta(minutes=10)


class PhoneVerificationOTP(models.Model):
    user = models.OneToOneField(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='phone_otp'
    )
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=otp_expiry)
    is_used = models.BooleanField(default=False)
    attempts = models.IntegerField(default=0)

    MAX_ATTEMPTS = 3

    def __str__(self):
        return f"OTP for {self.user.email}"

    @property
    def is_expired(self):
        return timezone.now() > self.expires_at

    @property
    def is_valid(self):
        return not self.is_used and not self.is_expired and self.attempts < self.MAX_ATTEMPTS

    def verify(self, code):
        """
        Attempt to verify the OTP code.
        Returns (success: bool, message: str)
        """
        if self.is_used:
            return False, 'This code has already been used.'
        if self.is_expired:
            return False, 'This code has expired. Please request a new one.'
        if self.attempts >= self.MAX_ATTEMPTS:
            return False, 'Maximum attempts exceeded. Please request a new code.'

        self.attempts += 1

        if self.otp != code:
            self.save()
            remaining = self.MAX_ATTEMPTS - self.attempts
            return False, f'Invalid code. {remaining} attempt(s) remaining.'

        self.is_used = True
        self.save()
        return True, 'Phone number verified successfully.'

    @classmethod
    def create_for_user(cls, user):
        """Create or replace OTP for a user."""
        cls.objects.filter(user=user).delete()
        return cls.objects.create(
            user=user,
            otp=generate_otp()
        )

    class Meta:
        verbose_name = 'Phone Verification OTP'
        verbose_name_plural = 'Phone Verification OTPs'