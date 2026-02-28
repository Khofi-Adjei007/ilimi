from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
    return redirect('accounts:login')