from django.urls import path
from . import views

urlpatterns = [
    path('words/', views.word_list, name='word_list'),
]