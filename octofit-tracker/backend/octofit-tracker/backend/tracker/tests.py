from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Team, AthleteProfile, ActivityLog


class TrackerModelTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Team A', description='Awesome team')
        self.athlete = AthleteProfile.objects.create(
            first_name='Jane', last_name='Doe', email='jane@example.com', team=self.team
        )
        self.activity = ActivityLog.objects.create(
            athlete=self.athlete,
            activity_type='run',
            duration_minutes=35,
            distance_km=7.1,
            date='2025-10-01',
        )

    def test_team_is_created(self):
        self.assertEqual(Team.objects.count(), 1)

    def test_athlete_is_created(self):
        self.assertEqual(AthleteProfile.objects.count(), 1)

    def test_activity_is_created(self):
        self.assertEqual(ActivityLog.objects.count(), 1)


class TrackerAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Team B', description='Second team')
        self.athlete = AthleteProfile.objects.create(
            first_name='John', last_name='Smith', email='john@example.com', team=self.team
        )

    def test_get_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)

    def test_get_athletes(self):
        response = self.client.get('/api/athletes/')
        self.assertEqual(response.status_code, 200)
