import logging
from django.shortcuts import redirect
from django.urls import reverse

logger = logging.getLogger(__name__)

EXEMPT_URLS = [
    '/admin/',
    '/api/',
    '/accounts/',
    '/onboarding/',
    '/static/',
    '/media/',
]


class OnboardingMiddleware:
    """
    Redirects authenticated school admins to the onboarding flow
    if their school setup is incomplete.

    Exempts: API routes, admin, auth pages, onboarding pages,
    static/media files.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if self._should_check(request):
            redirect_url = self._get_redirect(request)
            if redirect_url:
                return redirect(redirect_url)

        return self.get_response(request)

    def _should_check(self, request):
        """Return True only for authenticated users on non-exempt URLs."""
        if not request.user.is_authenticated:
            return False
        path = request.path
        for exempt in EXEMPT_URLS:
            if path.startswith(exempt):
                return False
        return True

    def _get_redirect(self, request):
        """Return redirect URL if onboarding is incomplete, else None."""
        try:
            membership = request.user.school_memberships.filter(
                role='school_admin', is_active=True
            ).select_related('school').first()

            if not membership:
                return None

            school = membership.school
            if not school.onboarding_complete:
                return reverse('tenants:onboarding_branch')

        except Exception as e:
            logger.warning(f"OnboardingMiddleware error for {request.user}: {e}")

        return None