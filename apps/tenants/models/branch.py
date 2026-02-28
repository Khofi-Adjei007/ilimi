from django.db import models


class Branch(models.Model):
    school = models.ForeignKey(
        'tenants.School',
        on_delete=models.CASCADE,
        related_name='branches'
    )
    name = models.CharField(max_length=255)
    branch_code = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    is_main_branch = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.school.name} — {self.name}'

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'
        ordering = ['-is_main_branch', 'name']
        unique_together = ['school', 'branch_code']