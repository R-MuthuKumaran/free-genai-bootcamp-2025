from django.test import TestCase
from .models import Word

class WordModelTest(TestCase):
    def setUp(self):
        Word.objects.create(parts={"word": "bonjour", "translation": "hello", "part_of_speech": "greeting"})

    def test_word_creation(self):
        word = Word.objects.get(parts__word="bonjour")
        self.assertEqual(word.parts["translation"], "hello")