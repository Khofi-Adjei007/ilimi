from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
def dashboard_home(request):
    context = {
        'user': request.user,
    }
    return render(request, 'dashboard/home.html', context)