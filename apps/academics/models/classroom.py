from django.db import models
from apps.tenants.models import School, Branch, SchoolMember
from .academic_year import AcademicYear
from .class_level import ClassLevel


class ClassRoom(models.Model):
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
        School, on_delete=models.CASCADE, related_name='classrooms'
    )
    branch = models.ForeignKey(
        Branch, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='classrooms'
    )
    academic_year = models.ForeignKey(
        AcademicYear, on_delete=models.CASCADE, related_name='classrooms'
    )
    class_level = models.ForeignKey(
        ClassLevel, on_delete=models.CASCADE, related_name='classrooms'
    )
    section_name = models.CharField(
        max_length=100,
        help_text="e.g. Nkrumah, Nightingale, A, B, Science, Business"
    )
    elective_group = models.CharField(
        max_length=20, choices=ELECTIVE_GROUP_CHOICES,
        blank=True, default='',
        help_text="For SHS elective streams only"
    )
    form_teacher = models.ForeignKey(
        SchoolMember, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='form_classes'
    )
    capacity = models.PositiveIntegerField(default=40)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('school', 'academic_year', 'class_level', 'section_name')
        ordering = ['class_level__order', 'section_name']

    def __str__(self):
        return f"{self.class_level.display_name} {self.section_name}"

    @property
    def full_name(self):
        return f"{self.class_level.display_name} {self.section_name}"