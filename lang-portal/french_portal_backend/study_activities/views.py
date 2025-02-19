from django.http import JsonResponse
from .models import StudyActivity

def study_activity_list(request):
    study_activities = StudyActivity.objects.all().values()
    return JsonResponse(list(study_activities), safe=False)