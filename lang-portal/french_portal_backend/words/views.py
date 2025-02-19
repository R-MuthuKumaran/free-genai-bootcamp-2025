from django.http import JsonResponse
from .models import Word

def word_list(request):
    words = Word.objects.all().values()
    return JsonResponse(list(words), safe=False)