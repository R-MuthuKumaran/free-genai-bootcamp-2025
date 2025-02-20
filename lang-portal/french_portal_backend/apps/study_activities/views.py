from django.http import JsonResponse
from rest_framework import viewsets
from .models import StudyActivity
from .serializers import StudyActivitySerializer

def study_activities_list(request):
    # Dummy data for example
    data = {
        "items": [
            {
                "id": 1,
                "name": "Vocabulary Quiz",
                "thumbnail_url": "https://demo.com/thumbnail.jpg",
                "description": "Practice your French vocabulary with interactive exercises"
            }
        ]
    }
    return JsonResponse(data)

def study_activity_detail(request, id):
    # Dummy data for example
    data = {
        "id": 1,
        "name": "Vocabulary Quiz",
        "thumbnail_url": "https://demo.com/thumbnail.jpg",
        "description": "Practice your French vocabulary with interactive exercises"
    }
    return JsonResponse(data)

def study_activity_sessions(request, id):
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
            "items_per_page": 20
        }
    }
    return JsonResponse(data)

def launch_study_activity(request):
    # Dummy data for example
    data = {
        "id": 333,
        "group_id": 222
    }
    return JsonResponse(data)

class StudyActivityViewSet(viewsets.ModelViewSet):
    queryset = StudyActivity.objects.all()
    serializer_class = StudyActivitySerializer