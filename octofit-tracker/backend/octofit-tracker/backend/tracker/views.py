from rest_framework import viewsets
from .models import Team, AthleteProfile, ActivityLog
from .serializers import TeamSerializer, AthleteProfileSerializer, ActivityLogSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class AthleteProfileViewSet(viewsets.ModelViewSet):
    queryset = AthleteProfile.objects.all()
    serializer_class = AthleteProfileSerializer


class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer
