from django.http import JsonResponse
from rest_framework import viewsets
from .models import Word, StudySession
from .serializers import WordSerializer, StudySessionSerializer

def last_study_session(request):
    # Dummy data for example
    data = {
        "id": 111,
        "group_id": 222,
        "created_at": "2025-02-08T17:20:23-05:00",
        "study_activity_id": 777,
        "group_name": "Salutations"
    }
    return JsonResponse(data)

def study_progress(request):
    # Dummy data for example
    data = {
        "total_words_studied": 30,
        "total_available_words": 324
    }
    return JsonResponse(data)

def quick_stats(request):
    # Dummy data for example
    data = {
        "success_rate": 75.0,
        "total_study_sessions": 6,
        "total_active_groups": 1,
        "study_streak_days": 2
    }
    return JsonResponse(data)

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class StudySessionViewSet(viewsets.ModelViewSet):
    queryset = StudySession.objects.all()
    serializer_class = StudySessionSerializer
