from django.http import JsonResponse
from rest_framework import viewsets
from .models import StudySession
from .serializers import StudySessionSerializer

def study_sessions_list(request):
    # Dummy data for example
    data = {
        "items": [
            {
                "id": 123,
                "activity_name": "Vocabulary Quiz",
                "group_name": "Salutations",
                "start_time": "2025-02-08T17:20:23-05:00",
                "end_time": "2025-02-08T17:30:23-05:00",
                "review_items_count": 20
            }
        ],
        "pagination": {
            "current_page": 1,
            "total_pages": 5,
            "total_items": 100,
            "items_per_page": 100
        }
    }
    return JsonResponse(data)

def study_session_detail(request, id):
    # Dummy data for example
    data = {
        "id": 123,
        "activity_name": "Vocabulary Quiz",
        "group_name": "Salutations",
        "start_time": "2025-02-08T17:20:23-05:00",
        "end_time": "2025-02-08T17:30:23-05:00",
        "review_items_count": 20
    }
    return JsonResponse(data)

def study_session_words(request, id):
    # Dummy data for example
    data = {
        "items": [
            {
                "french": "bonjour",
                "english": "hello",
                "correct_count": 5,
                "wrong_count": 2
            }
        ],
        "pagination": {
            "current_page": 1,
            "total_pages": 1,
            "total_items": 20,
            "items_per_page": 100
        }
    }
    return JsonResponse(data)

class StudySessionViewSet(viewsets.ModelViewSet):
    queryset = StudySession.objects.all()
    serializer_class = StudySessionSerializer
