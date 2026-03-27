from django.contrib import admin
from .models import Team, AthleteProfile, ActivityLog, Leaderboard, Workout


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')


@admin.register(AthleteProfile)
class AthleteProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'team', 'joined_at')


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('athlete', 'activity_type', 'duration_minutes', 'date', 'created_at')


    @admin.register(Leaderboard)
    class LeaderboardAdmin(admin.ModelAdmin):
        list_display = ('team', 'total_points', 'updated_at')


    @admin.register(Workout)
    class WorkoutAdmin(admin.ModelAdmin):
        list_display = ('name', 'duration_minutes', 'created_by', 'created_at')
