from django.db import models
from apps.tenants.models import SchoolMember
from .classroom import ClassRoom
from .subject import Subject
from .term import Term


class SubjectAssignment(models.Model):
    classroom = models.ForeignKey(
        ClassRoom, on_delete=models.CASCADE, related_name='subject_assignments'
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='assignments'
    )
    teacher = models.ForeignKey(
        SchoolMember, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='subject_assignments'
    )
    term = models.ForeignKey(
        Term, on_delete=models.CASCADE, related_name='subject_assignments'
    )
    periods_per_week = models.PositiveIntegerField(default=5)

    class Meta:
        unique_together = ('classroom', 'subject', 'term')
        ordering = ['classroom', 'subject__name']

    def __str__(self):
        teacher_name = self.teacher.user.full_name if self.teacher else 'Unassigned'
        return f"{self.subject.name} — {self.classroom} — {teacher_name}"