from django.urls import path
from . import views

urlpatterns = [
    path('study_sessions/', views.study_session_list, name='study_session_list'),
]