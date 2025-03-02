from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WordViewSet

router = DefaultRouter()
router.register(r'words', WordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
