from django.db import models
from apps.tenants.models import School


class ClassLevel(models.Model):
    LEVEL_CHOICES = [
        ('nursery_1', 'Nursery 1'),
        ('nursery_2', 'Nursery 2'),
        ('kindergarten_1', 'Kindergarten 1'),
        ('kindergarten_2', 'Kindergarten 2'),
        ('primary_1', 'Primary 1'),
        ('primary_2', 'Primary 2'),
        ('primary_3', 'Primary 3'),
        ('primary_4', 'Primary 4'),
        ('primary_5', 'Primary 5'),
        ('primary_6', 'Primary 6'),
        ('jhs_1', 'JHS 1'),
        ('jhs_2', 'JHS 2'),
        ('jhs_3', 'JHS 3'),
        ('shs_1', 'SHS 1'),
        ('shs_2', 'SHS 2'),
        ('shs_3', 'SHS 3'),
        ('other', 'Other'),
    ]

    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='class_levels'
    )
    name = models.CharField(max_length=30, choices=LEVEL_CHOICES)
    custom_name = models.CharField(
        max_length=100, blank=True,
        help_text="Override display name if needed e.g. 'Form 1'"
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('school', 'name')
        ordering = ['order', 'name']

    def __str__(self):
        return self.custom_name or self.get_name_display()

    @property
    def display_name(self):
        return self.custom_name or self.get_name_display()