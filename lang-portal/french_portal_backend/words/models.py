from django.db import models
from groups.models import Group

class Word(models.Model):
    id = models.AutoField(primary_key=True)
    parts = models.JSONField()

    def __str__(self):
        return str(self.id)

class WordGroup(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.ForeignKey('Word', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.word.id} - {self.group.name}"