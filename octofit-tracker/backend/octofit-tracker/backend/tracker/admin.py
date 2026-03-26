from django.contrib import admin
from .models import Team, AthleteProfile, ActivityLog


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')


@admin.register(AthleteProfile)
class AthleteProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'team', 'joined_at')


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('athlete', 'activity_type', 'duration_minutes', 'date', 'created_at')
