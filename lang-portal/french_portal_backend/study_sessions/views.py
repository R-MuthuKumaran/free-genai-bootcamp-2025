from django.http import JsonResponse
from .models import StudySession

def study_session_list(request):
    study_sessions = StudySession.objects.all().values()
    return JsonResponse(list(study_sessions), safe=False)