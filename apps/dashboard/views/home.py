import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

ROLE_PORTAL_MAP = {
    'school_admin': 'dashboard:admin_portal',
    'branch_manager': 'dashboard:admin_portal',
    'teacher': 'dashboard:teacher_portal',
    'accountant': 'dashboard:accountant_portal',
    'receptionist': 'dashboard:receptionist_portal',
}


@login_required(login_url='accounts:login')
def dashboard_home(request):
    """
    Role-aware router — redirects authenticated users to their
    role-specific portal based on their SchoolMember role.
    """
    from apps.tenants.models import SchoolMember

    membership = SchoolMember.objects.filter(
        user=request.user, is_active=True
    ).select_related('school').first()

    if not membership:
        logger.warning(f"User {request.user.email} has no active school membership.")
        return render(request, 'dashboard/no_membership.html', {'user': request.user})

    portal_url = ROLE_PORTAL_MAP.get(membership.role)

    if not portal_url:
        logger.warning(f"Unknown role {membership.role} for user {request.user.email}")
        return render(request, 'dashboard/no_membership.html', {'user': request.user})

    return redirect(portal_url)