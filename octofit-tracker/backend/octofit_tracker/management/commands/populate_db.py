from django.core.management.base import BaseCommand
from tracker.models import Team, AthleteProfile, ActivityLog
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        ActivityLog.objects.all().delete()
        AthleteProfile.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        ironman = AthleteProfile.objects.create(first_name='Tony', last_name='Stark', email='ironman@marvel.com', team=marvel)
        spiderman = AthleteProfile.objects.create(first_name='Peter', last_name='Parker', email='spiderman@marvel.com', team=marvel)
        batman = AthleteProfile.objects.create(first_name='Bruce', last_name='Wayne', email='batman@dc.com', team=dc)
        wonderwoman = AthleteProfile.objects.create(first_name='Diana', last_name='Prince', email='wonderwoman@dc.com', team=dc)

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        ActivityLog.objects.create(athlete=ironman, activity_type='run', duration_minutes=30, distance_km=5, date='2026-03-01')
        ActivityLog.objects.create(athlete=spiderman, activity_type='cycle', duration_minutes=45, distance_km=20, date='2026-03-02')
        ActivityLog.objects.create(athlete=batman, activity_type='workout', duration_minutes=60, date='2026-03-03')
        ActivityLog.objects.create(athlete=wonderwoman, activity_type='swim', duration_minutes=50, distance_km=2, date='2026-03-04')

        self.stdout.write(self.style.SUCCESS('Ensuring unique index on email for users...'))
        with connection.cursor() as cursor:
            cursor.execute('''
                db = connection.connection.get_database()
                db.athleteprofile.create_index([('email', 1)], unique=True)
            ''')

        self.stdout.write(self.style.SUCCESS('Test data created for Marvel and DC teams!'))
