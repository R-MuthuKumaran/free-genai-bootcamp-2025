from django.db import models
from words.models import Word

class StudySession(models.Model):
    id = models.AutoField(primary_key=True)
    study_activity = models.ForeignKey('study_activities.StudyActivity', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class WordReviewItem(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)