import os
import logging

# Crear el directorio de logs si no existe
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=os.path.join(log_dir, 'app.log'), 
    level=logging.ERROR,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def log_error(message):
    """
    Registra un mensaje de error en el archivo de log.
    """
    logging.error(message)

def validate_username(username):
    """
    Valida que el nombre de usuario no esté vacío y cumpla con ciertos criterios.
    """
    if not username:
        raise ValueError("El nombre de usuario no puede estar vacío.")
    # Aquí puedes agregar más validaciones si es necesario
    return True

def transform_character_data(character):
    """
    Transforma los datos del personaje en un formato deseado.
    """
    return {
        'name': character.get('name', 'N/A'),
        'status': character.get('status', 'N/A'),
        'species': character.get('species', 'N/A'),
        'image': character.get('image', '')
    }

def format_character_display(character):
    """
    Formatea los datos del personaje para su visualización.
    """
    return f"Nombre: {character['name']}\nEstatus: {character['status']}\nEspecie: {character['species']}"

# Ejemplo de uso de funciones utilitarias
if __name__ == "__main__":
    try:
        # Simulando una validación de nombre de usuario
        validate_username("admin")
    except ValueError as ve:
        log_error(f"Validation Error: {ve}")
