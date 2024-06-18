import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import os
from src.api import RickAndMortyAPI

class MainScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Rick and Morty App - Main")
        self.create_main_screen()

    def create_main_screen(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.fetch_button = tk.Button(self.main_frame, text="Fetch Characters", command=self.fetch_characters)
        self.fetch_button.pack(pady=10)

        self.character_list = tk.Listbox(self.main_frame)
        self.character_list.pack(pady=10)
        self.character_list.bind("<<ListboxSelect>>", self.display_character)

        self.character_image = tk.Label(self.main_frame)
        self.character_image.pack(pady=10)

    def fetch_characters(self):
        try:
            characters = RickAndMortyAPI.fetch_characters()
            self.characters = [self.transform_character_data(char) for char in characters]
            self.character_list.delete(0, tk.END)
            for character in self.characters:
                self.character_list.insert(tk.END, character['name'])
        except requests.RequestException as e:
            from src.utils import log_error  # Importación diferida
            log_error(f"API Error: {e}")
            messagebox.showerror("API Error", f"Failed to fetch data: {e}")

    def display_character(self, event):
        selected_index = self.character_list.curselection()[0]
        character = self.characters[selected_index]

        try:
            print(f"Fetching image from: {character['image']}")  # Línea de depuración
            image_data = RickAndMortyAPI.fetch_character_image(character['image'])

            # Guardar la imagen localmente
            image_path = f"assets/images/{character['name'].replace(' ', '_')}.png"
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            with open(image_path, 'wb') as f:
                f.write(image_data)
            print(f"Image saved at: {image_path}")  # Línea de depuración

            # Mostrar la imagen en la interfaz utilizando PIL
            image = Image.open(image_path)
            image = image.resize((200, 200), Image.LANCZOS)  # Redimensionar la imagen
            image.show()

            character_info = self.format_character_display(character)
            messagebox.showinfo("Character Info", character_info)
        except requests.RequestException as e:
            from src.utils import log_error  # Importación diferida
            log_error(f"Image Error: {e}")
            messagebox.showerror("Image Error", f"Failed to fetch image: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            messagebox.showerror("Error", f"Failed to display image: {e}")


    @staticmethod
    def transform_character_data(character):
        return {
            'name': character.get('name', 'N/A'),
            'status': character.get('status', 'N/A'),
            'species': character.get('species', 'N/A'),
            'image': character.get('image', '')
        }

    @staticmethod
    def format_character_display(character):
        return f"Nombre: {character['name']}\nEstatus: {character['status']}\nEspecie: {character['species']}"

if __name__ == "__main__":
    root = tk.Tk()
    app = MainScreen(root)
    root.mainloop()
