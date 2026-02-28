from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from apps.accounts.forms import LoginForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    form = LoginForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'dashboard:home')
                return redirect(next_url)
        else:
            messages.error(request, 'Invalid email or password.')

    context = {
        'form': form,
        'features': [
            'Multi-branch school management',
            'Fee collection with Mobile Money',
            'SMS notifications for parents',
            'Role-based access control',
        ]
    }

    return render(request, 'accounts/login.html', context)