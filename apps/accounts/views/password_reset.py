from django.shortcuts import render, redirect
from django.contrib import messages
from apps.accounts.forms import PasswordResetRequestForm, SetNewPasswordForm


def password_reset_request(request):
    form = PasswordResetRequestForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            messages.success(
                request,
                'If an account exists with that email, '
                'you will receive reset instructions shortly.'
            )
            return redirect('accounts:login')

    return render(request, 'accounts/password_reset.html', {'form': form})


def set_new_password(request, token):
    form = SetNewPasswordForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            messages.success(
                request,
                'Your password has been reset successfully. Please log in.'
            )
            return redirect('accounts:login')

    return render(request, 'accounts/set_new_password.html', {'form': form})