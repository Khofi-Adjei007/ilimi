import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from apps.accounts.forms import OTPVerificationForm
from apps.accounts.models import User

logger = logging.getLogger(__name__)


def verify_phone(request):
    """Verify phone number via SMS OTP."""
    user_id = request.session.get('pending_verification_user_id')
    if not user_id:
        messages.error(request, 'Session expired. Please register again.')
        return redirect('accounts:register_step1')

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        messages.error(request, 'User not found. Please register again.')
        return redirect('accounts:register_step1')

    form = OTPVerificationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            from apps.accounts.services.verification import verify_phone_otp
            otp_code = form.cleaned_data['otp']
            success, message = verify_phone_otp(user, otp_code)

            if success:
                # Clear session
                del request.session['pending_verification_user_id']
                # Log user in
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, 'Phone verified! Let\'s set up your school.')
                return redirect('tenants:onboarding_branch')
            else:
                messages.error(request, message)

    context = {
        'form': form,
        'phone_number': user.phone_number,
        'masked_phone': f"{'*' * (len(user.phone_number) - 4)}{user.phone_number[-4:]}",
    }
    return render(request, 'accounts/verify_phone.html', context)


def resend_otp(request):
    """Resend OTP to user's phone."""
    user_id = request.session.get('pending_verification_user_id')
    if not user_id:
        return redirect('accounts:register_step1')

    try:
        user = User.objects.get(id=user_id)
        from apps.accounts.services.registration import resend_otp as resend
        success, message = resend(user)
        if success:
            messages.success(request, message)
        else:
            messages.error(request, message)
    except User.DoesNotExist:
        messages.error(request, 'User not found.')

    return redirect('accounts:verify_phone')