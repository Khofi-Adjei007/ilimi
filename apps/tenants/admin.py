from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SubscriptionPlan, School, Branch, SchoolMember


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'plan_type', 'max_branches', 'max_students', 'price_monthly', 'is_active']
    list_filter = ['is_active', 'plan_type']


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'city', 'subscription_status', 'is_active', 'created_at']
    list_filter = ['subscription_status', 'is_active', 'country']
    search_fields = ['name', 'email']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'school', 'city', 'is_main_branch', 'is_active']
    list_filter = ['is_main_branch', 'is_active']
    search_fields = ['name', 'school__name']


@admin.register(SchoolMember)
class SchoolMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'school', 'branch', 'role', 'is_active', 'joined_at']
    list_filter = ['role', 'is_active']
    search_fields = ['user__email', 'school__name']