from rest_framework import serializers
from .models import Team, AthleteProfile, ActivityLog, Leaderboard, Workout


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class AthleteProfileSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)

    class Meta:
        model = AthleteProfile
        fields = '__all__'


class ActivityLogSerializer(serializers.ModelSerializer):
    athlete = AthleteProfileSerializer(read_only=True)

    class Meta:
        model = ActivityLog
        fields = '__all__'


class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)

    class Meta:
        model = Leaderboard
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    created_by = AthleteProfileSerializer(read_only=True)

    class Meta:
        model = Workout
        fields = '__all__'
