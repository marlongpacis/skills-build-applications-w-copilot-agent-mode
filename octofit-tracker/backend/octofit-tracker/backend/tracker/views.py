from rest_framework import viewsets
from .models import Team, AthleteProfile, ActivityLog
from .models import Leaderboard, Workout
from .serializers import TeamSerializer, AthleteProfileSerializer, ActivityLogSerializer, LeaderboardSerializer, WorkoutSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class AthleteProfileViewSet(viewsets.ModelViewSet):
    queryset = AthleteProfile.objects.all()
    serializer_class = AthleteProfileSerializer


class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer


# Leaderboard ViewSet
class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


# Workout ViewSet
class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
