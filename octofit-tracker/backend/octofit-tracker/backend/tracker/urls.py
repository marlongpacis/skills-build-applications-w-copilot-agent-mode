from rest_framework import routers
from .views import TeamViewSet, AthleteProfileViewSet, ActivityLogViewSet

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'athletes', AthleteProfileViewSet)
router.register(r'activities', ActivityLogViewSet)

urlpatterns = router.urls
