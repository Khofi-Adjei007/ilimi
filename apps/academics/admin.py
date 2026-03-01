from django.contrib import admin
from apps.academics.models import (
    AcademicYear, Term, ClassLevel, ClassRoom, Subject, SubjectAssignment
)


@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ['name', 'school', 'start_date', 'end_date', 'is_current']
    list_filter = ['school', 'is_current']
    search_fields = ['name', 'school__name']


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ['get_name_display', 'academic_year', 'start_date', 'end_date', 'is_current']
    list_filter = ['academic_year__school', 'is_current']
    search_fields = ['academic_year__name']


@admin.register(ClassLevel)
class ClassLevelAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'school', 'order', 'is_active']
    list_filter = ['school', 'is_active']
    search_fields = ['name', 'custom_name', 'school__name']


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'school', 'academic_year', 'branch', 'form_teacher', 'capacity', 'is_active']
    list_filter = ['school', 'academic_year', 'is_active']
    search_fields = ['section_name', 'class_level__name', 'school__name']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'subject_type', 'school', 'is_active']
    list_filter = ['school', 'subject_type', 'is_active']
    search_fields = ['name', 'code', 'school__name']


@admin.register(SubjectAssignment)
class SubjectAssignmentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'classroom', 'teacher', 'term', 'periods_per_week']
    list_filter = ['classroom__school', 'term']
    search_fields = ['subject__name', 'classroom__section_name']