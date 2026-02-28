from django.db import models
from django.utils.text import slugify


class School(models.Model):
    STATUS_CHOICES = [
        ('trial', 'Trial'),
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('cancelled', 'Cancelled'),
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='Ghana')
    logo = models.ImageField(upload_to='schools/logos/', blank=True, null=True)
    website = models.URLField(blank=True)
    subscription_plan = models.ForeignKey(
        'tenants.SubscriptionPlan',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='schools'
    )
    subscription_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='trial'
    )
    trial_ends_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'
        ordering = ['name']