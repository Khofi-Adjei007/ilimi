from django.db import models
from apps.tenants.models import School


class Subject(models.Model):
    SUBJECT_TYPE_CHOICES = [
        ('core', 'Core'),
        ('elective', 'Elective'),
        ('optional', 'Optional'),
    ]

    ELECTIVE_GROUP_CHOICES = [
        ('', 'None / N/A'),
        ('science', 'Science'),
        ('business', 'Business'),
        ('arts', 'General Arts'),
        ('home_economics', 'Home Economics'),
        ('visual_arts', 'Visual Arts'),
        ('technical', 'Technical'),
        ('agriculture', 'Agriculture'),
    ]

    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='subjects'
    )
    name = models.CharField(max_length=100)
    code = models.CharField(
        max_length=20, blank=True,
        help_text="Short code e.g. MATH, ENG, SCI"
    )
    subject_type = models.CharField(
        max_length=10, choices=SUBJECT_TYPE_CHOICES, default='core'
    )
    elective_group = models.CharField(
        max_length=20, choices=ELECTIVE_GROUP_CHOICES,
        blank=True, default='',
        help_text="For elective subjects — which SHS stream this belongs to"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('school', 'name')
        ordering = ['subject_type', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_subject_type_display()})"