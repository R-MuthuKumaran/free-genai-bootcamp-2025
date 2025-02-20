from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WordViewSet, StudySessionViewSet

router = DefaultRouter()
router.register(r'words', WordViewSet)
router.register(r'study_sessions', StudySessionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]