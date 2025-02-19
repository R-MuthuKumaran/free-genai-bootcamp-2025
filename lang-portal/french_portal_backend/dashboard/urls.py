from django.urls import path
from . import views

urlpatterns = [
    path('last_study_session/', views.last_study_session, name='last_study_session'),
    path('study_progress/', views.study_progress, name='study_progress'),
]