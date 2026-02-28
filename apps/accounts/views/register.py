import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from apps.accounts.forms import RegistrationStep1Form, RegistrationStep2Form

logger = logging.getLogger(__name__)


def register_step1(request):
    """Step 1 — Personal information."""
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    form = RegistrationStep1Form(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Store step 1 data in session
            request.session['registration_step1'] = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'phone_number': form.cleaned_data['phone_number'],
                'password1': form.cleaned_data['password1'],
            }
            return redirect('accounts:register_step2')

    return render(request, 'accounts/register_step1.html', {'form': form})


def register_step2(request):
    """Step 2 — School information."""
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    # Ensure step 1 was completed
    step1_data = request.session.get('registration_step1')
    if not step1_data:
        messages.error(request, 'Please complete step 1 first.')
        return redirect('accounts:register_step1')

    form = RegistrationStep2Form(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            from apps.accounts.services.registration import create_user_account
            from apps.tenants.services.onboarding import create_school_with_owner

            try:
                user, otp = create_user_account(step1_data)
                school_data = form.cleaned_data
                create_school_with_owner(user, school_data)

                # Store user id in session for verification
                request.session['pending_verification_user_id'] = user.id
                # Clear step 1 data
                del request.session['registration_step1']

                messages.success(
                    request,
                    f'Account created! We sent a 6-digit code to {user.phone_number}.'
                )
                return redirect('accounts:verify_phone')

            except Exception as e:
                logger.error(f"Registration error: {str(e)}")
                messages.error(request, 'Something went wrong. Please try again.')

    context = {
        'form': form,
        'step1_data': step1_data,
    }
    return render(request, 'accounts/register_step2.html', context)