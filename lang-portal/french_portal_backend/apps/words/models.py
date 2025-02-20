from django.db import models

class Word(models.Model):
    french = models.CharField(max_length=100)
    english = models.CharField(max_length=100)
    correct_count = models.IntegerField(default=0)
    wrong_count = models.IntegerField(default=0)