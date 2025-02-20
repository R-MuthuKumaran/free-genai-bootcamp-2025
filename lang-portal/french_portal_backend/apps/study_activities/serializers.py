from rest_framework import serializers
from .models import StudyActivity

class StudyActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyActivity
        fields = '__all__'