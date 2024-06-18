import requests
from src.utils import log_error  # Importar directamente desde utils.py

class RickAndMortyAPI:
    BASE_URL = "https://rickandmortyapi.com/api/character"

    @staticmethod
    def fetch_characters():
        try:
            response = requests.get(RickAndMortyAPI.BASE_URL)
            response.raise_for_status()  # Lanza una excepción si la petición falló
            data = response.json()
            return data['results']
        except requests.RequestException as e:
            log_error(f"API Error in fetch_characters: {e}")
            raise

    @staticmethod
    def fetch_character_image(image_url):
        try:
            response = requests.get(image_url)
            response.raise_for_status()  # Lanza una excepción si la petición falló
            return response.content
        except requests.RequestException as e:
            log_error(f"API Error in fetch_character_image: {e}")
            raise
