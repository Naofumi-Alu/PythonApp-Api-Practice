import unittest
from unittest.mock import patch, call
from src.api import RickAndMortyAPI
from src.utils import log_error
import requests

class TestRickAndMortyAPI(unittest.TestCase):
    @patch('src.api.requests.get')
    def test_fetch_characters_success(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'results': [
                {'name': 'Rick Sanchez', 'image': 'https://rickandmortyapi.com/api/character/avatar/1.jpeg'},
                {'name': 'Morty Smith', 'image': 'https://rickandmortyapi.com/api/character/avatar/2.jpeg'}
            ]
        }
        mock_get.return_value = mock_response

        characters = RickAndMortyAPI.fetch_characters()
        self.assertEqual(len(characters), 2)
        self.assertEqual(characters[0]['name'], 'Rick Sanchez')

    @patch('src.api.requests.get')
    @patch('src.utils.log_error')
    def test_fetch_characters_api_error(self, mock_log_error, mock_get):
        mock_get.side_effect = requests.RequestException("API Error")
        with self.assertRaises(requests.RequestException):
            RickAndMortyAPI.fetch_characters()
        mock_log_error.assert_called_once_with("API Error in fetch_characters: API Error")

    @patch('src.api.requests.get')
    def test_fetch_character_image_success(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.content = b'image data'
        mock_get.return_value = mock_response

        image_data = RickAndMortyAPI.fetch_character_image('https://rickandmortyapi.com/api/character/avatar/1.jpeg')
        self.assertEqual(image_data, b'image data')

    @patch('src.api.requests.get')
    @patch('src.utils.log_error')
    def test_fetch_character_image_api_error(self, mock_log_error, mock_get):
        mock_get.side_effect = requests.RequestException("API Error")
        with self.assertRaises(requests.RequestException):
            RickAndMortyAPI.fetch_character_image('https://rickandmortyapi.com/api/character/avatar/1.jpeg')
        mock_log_error.assert_called_once_with("API Error in fetch_character_image: API Error")

if __name__ == "__main__":
    unittest.main()
