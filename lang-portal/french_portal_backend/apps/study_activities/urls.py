from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudyActivityViewSet

router = DefaultRouter()
router.register(r'study_activities', StudyActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]