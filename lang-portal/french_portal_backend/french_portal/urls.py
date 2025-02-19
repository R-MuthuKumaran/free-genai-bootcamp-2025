from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('health/', lambda request: HttpResponse('OK')),
    path('admin/', admin.site.urls),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/', include('words.urls')),
    path('api/', include('groups.urls')),
    path('api/', include('study_sessions.urls')),
    path('api/', include('study_activities.urls')),
]