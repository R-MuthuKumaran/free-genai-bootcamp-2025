from django.db import models

class StudyActivity(models.Model):
    name = models.CharField(max_length=100)
    thumbnail_url = models.URLField()
    description = models.TextField()