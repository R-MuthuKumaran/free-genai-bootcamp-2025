from django.http import JsonResponse
from .models import Group

def group_list(request):
    groups = Group.objects.all().values()
    return JsonResponse(list(groups), safe=False)