from django.db import models
from apps.tenants.models import School


class AcademicYear(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='academic_years'
    )
    name = models.CharField(max_length=20)  # e.g. "2025/2026"
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('school', 'name')
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.school.name} — {self.name}"

    def save(self, *args, **kwargs):
        # Only one current academic year per school
        if self.is_current:
            AcademicYear.objects.filter(
                school=self.school, is_current=True
            ).exclude(pk=self.pk).update(is_current=False)
        super().save(*args, **kwargs)