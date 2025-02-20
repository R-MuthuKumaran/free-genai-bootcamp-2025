from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudySessionViewSet

router = DefaultRouter()
router.register(r'study_sessions', StudySessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
