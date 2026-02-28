from django.db import models


class SubscriptionPlan(models.Model):
    PLAN_CHOICES = [
        ('free', 'Free Trial'),
        ('basic', 'Basic'),
        ('pro', 'Pro'),
        ('enterprise', 'Enterprise'),
    ]

    name = models.CharField(max_length=100)
    plan_type = models.CharField(max_length=20, choices=PLAN_CHOICES, unique=True)
    max_branches = models.PositiveIntegerField(default=1)
    max_students = models.PositiveIntegerField(default=100)
    price_monthly = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_yearly = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subscription Plan'
        verbose_name_plural = 'Subscription Plans'
        ordering = ['price_monthly']