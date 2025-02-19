import os
import json
import django
from invoke import task
from pathlib import Path

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'french_portal_backend.french_portal.settings')
django.setup()

# Now we can import Django models
from words.models import Word
from django.core.management import call_command

@task
def init_db(ctx):
    """Initialize the database and create tables"""
    print('Creating database...')
    call_command('makemigrations')
    call_command('migrate')
    print('Database initialized successfully.')

@task
def seed_db(ctx):
    """Seed the database with initial data"""
    try:
        # First ensure database is initialized
        init_db(ctx)
        
        seed_file = Path('db/seeds/french_words_seed.json')
        if not seed_file.exists():
            print(f'Error: Seed file not found at {seed_file}')
            return

        with open(seed_file) as f:
            words_data = json.load(f)
            for word_data in words_data:
                # Transform the data to match our model
                french = word_data['parts']['word']
                english = word_data['parts']['translation']
                parts = {
                    'part_of_speech': word_data['parts']['part_of_speech']
                }
                
                # Create or update the word
                Word.objects.update_or_create(
                    id=word_data['id'],
                    defaults={
                        'french': french,
                        'english': english,
                        'parts': parts
                    }
                )
        print('Database seeded successfully.')
    except Exception as e:
        print(f'Error seeding database: {str(e)}')
