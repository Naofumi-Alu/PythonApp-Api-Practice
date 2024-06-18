import unittest
import tkinter as tk
from unittest.mock import patch
from src.main_screen import MainScreen
from src.api import RickAndMortyAPI

class TestMainScreen(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = MainScreen(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch.object(RickAndMortyAPI, 'fetch_characters')
    def test_fetch_characters_success(self, mock_fetch_characters):
        mock_fetch_characters.return_value = [
            {'name': 'Rick Sanchez', 'image': 'https://rickandmortyapi.com/api/character/avatar/1.jpeg'},
            {'name': 'Morty Smith', 'image': 'https://rickandmortyapi.com/api/character/avatar/2.jpeg'}
        ]

        self.app.fetch_characters()
        self.assertEqual(self.app.character_list.size(), 2)

    @patch.object(RickAndMortyAPI, 'fetch_characters')
    def test_fetch_characters_failure(self, mock_fetch_characters):
        mock_fetch_characters.side_effect = Exception("API Error")

        self.app.fetch_characters()
        self.assertEqual(self.app.character_list.size(), 0)

    @patch.object(RickAndMortyAPI, 'fetch_character_image')
    @patch.object(RickAndMortyAPI, 'fetch_characters')
    def test_display_character(self, mock_fetch_characters, mock_fetch_character_image):
        mock_fetch_characters.return_value = [
            {'name': 'Rick Sanchez', 'image': 'https://rickandmortyapi.com/api/character/avatar/1.jpeg'},
            {'name': 'Morty Smith', 'image': 'https://rickandmortyapi.com/api/character/avatar/2.jpeg'}
        ]
        # Proporcionar datos de imagen simulados que sean válidos
        mock_fetch_character_image.return_value = (
            b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10'
            b'\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\rIDATx\x9ccddbf\xa0'
            b'\x040Q\x00\x00\x01\x02\x00\x01\xe2&\x05\xa3\x00\x00\x00\x00IEND\xaeB`\x82'
        )

        self.app.fetch_characters()
        self.app.character_list.select_set(0)  # Selecciona el primer elemento
        self.app.display_character(None)  # Llama a display_character sin evento real
        self.assertIsNotNone(self.app.character_image.image)

if __name__ == "__main__":
    unittest.main()
