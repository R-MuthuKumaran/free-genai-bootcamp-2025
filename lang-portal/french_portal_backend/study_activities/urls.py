from django.urls import path
from . import views

urlpatterns = [
    path('study_activities/', views.study_activity_list, name='study_activity_list'),
]