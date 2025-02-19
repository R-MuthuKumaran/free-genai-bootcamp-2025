from django.http import JsonResponse
from study_sessions.models import StudySession
from groups.models import Group

def last_study_session(request):
    last_session = StudySession.objects.last()
    if last_session:
        response = {
            "id": last_session.id,
            "group_name": last_session.study_activity.group.name
        }
    else:
        response = {}
    return JsonResponse(response)

def study_progress(request):
    # Placeholder for actual implementation
    response = {
        # Add actual progress metrics here
    }
    return JsonResponse(response)