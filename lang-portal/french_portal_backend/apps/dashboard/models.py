from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=100)
    definition = models.TextField()
    example = models.TextField()

class StudySession(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()
    correct_answers = models.IntegerField()
    incorrect_answers = models.IntegerField()