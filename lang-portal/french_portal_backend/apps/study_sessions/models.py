from django.db import models

class StudySession(models.Model):
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    study_activity = models.ForeignKey('study_activities.StudyActivity', on_delete=models.CASCADE)