from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.urls import path, include
from .views import TeamViewSet, AthleteProfileViewSet, ActivityLogViewSet, LeaderboardViewSet, WorkoutViewSet

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'athletes', AthleteProfileViewSet)
router.register(r'activities', ActivityLogViewSet)
router.register(r'leaderboards', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'teams': reverse('team-list', request=request, format=format),
		'athletes': reverse('athleteprofile-list', request=request, format=format),
		'activities': reverse('activitylog-list', request=request, format=format),
		'leaderboards': reverse('leaderboard-list', request=request, format=format),
		'workouts': reverse('workout-list', request=request, format=format),
	})

urlpatterns = [
	path('', api_root, name='api-root'),
	path('', include(router.urls)),
]
