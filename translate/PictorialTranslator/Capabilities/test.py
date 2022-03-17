import os, sys
import unittest
from chalicelib import translation_service


class TranslationServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = translation_service.TranslationService()

    def test_translate_text(self):
        translation = self.service.translate_text('Einbahnstrabe')
        self.assertTrue(translation)
        self.assertEqual('de', translation['sourceLanguage'])
        self.assertEqual('one-way street', translation['translatedText'])

if __name__ == "__main__":
    unittest.main()