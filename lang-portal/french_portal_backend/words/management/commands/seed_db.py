import json
from django.core.management.base import BaseCommand
from words.models import Word

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        with open('db/seeds/french_words_seed.json') as f:
            words_data = json.load(f)
            for word_data in words_data:
                Word.objects.create(**word_data)
        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))