from rest_framework import serializers
from .models import Team, AthleteProfile, ActivityLog


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
