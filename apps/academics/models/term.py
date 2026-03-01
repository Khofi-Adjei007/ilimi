from django.db import models
from .academic_year import AcademicYear


class Term(models.Model):
    TERM_CHOICES = [
        ('term_1', 'Term 1'),
        ('term_2', 'Term 2'),
        ('term_3', 'Term 3'),
    ]

    academic_year = models.ForeignKey(
        AcademicYear, on_delete=models.CASCADE, related_name='terms'
    )
    name = models.CharField(max_length=10, choices=TERM_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)

    class Meta:
        unique_together = ('academic_year', 'name')
        ordering = ['name']

    def __str__(self):
        return f"{self.academic_year.name} — {self.get_name_display()}"

    def save(self, *args, **kwargs):
        # Only one current term per academic year
        if self.is_current:
            Term.objects.filter(
                academic_year=self.academic_year, is_current=True
            ).exclude(pk=self.pk).update(is_current=False)
        super().save(*args, **kwargs)