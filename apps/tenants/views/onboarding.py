import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.tenants.forms import BranchSetupForm

logger = logging.getLogger(__name__)


@login_required(login_url='accounts:login')
def onboarding_branch(request):
    """Onboarding step — set up first branch."""
    membership = request.user.school_memberships.filter(
        role='school_admin', is_active=True
    ).select_related('school').first()

    if not membership:
        messages.error(request, 'No school found for your account.')
        return redirect('accounts:login')

    school = membership.school

    if school.onboarding_complete:
        return redirect('dashboard:home')

    form = BranchSetupForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            from apps.tenants.services.onboarding import create_main_branch, complete_onboarding
            try:
                create_main_branch(school, form.cleaned_data)
                complete_onboarding(school, request.user)
                return redirect('tenants:onboarding_complete')
            except Exception as e:
                logger.error(f"Branch setup error: {str(e)}")
                messages.error(request, 'Something went wrong. Please try again.')

    context = {
        'form': form,
        'school': school,
    }
    return render(request, 'tenants/onboarding_branch.html', context)


@login_required(login_url='accounts:login')
def onboarding_complete(request):
    """Onboarding complete — welcome screen."""
    membership = request.user.school_memberships.filter(
        role='school_admin', is_active=True
    ).select_related('school').first()

    school = membership.school if membership else None

    steps = [
        ('Your Details', 'Tell us about yourself.'),
        ('School Info', 'About your school.'),
        ('Verify Phone', 'Confirm your number.'),
        ('Branch Setup', 'Your first campus.'),
    ]

    return render(request, 'tenants/onboarding_complete.html', {
        'school': school,
        'user': request.user,
        'steps': steps,
    })