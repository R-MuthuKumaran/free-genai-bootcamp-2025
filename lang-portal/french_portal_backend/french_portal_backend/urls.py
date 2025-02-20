from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('health/', lambda request: HttpResponse('OK')),
    path('admin/', admin.site.urls),
    path('api/dashboard/', include('apps.dashboard.urls')),
    path('api/words/', include('apps.words.urls')),
    path('api/groups/', include('apps.groups.urls')),
    path('api/study_sessions/', include('apps.study_sessions.urls')),
    path('api/study_activities/', include('apps.study_activities.urls')),
]