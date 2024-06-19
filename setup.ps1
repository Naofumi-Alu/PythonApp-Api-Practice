# setup.ps1
# Crea y activa un entorno virtual e instala las dependencias

# Crear y activar el entorno virtual
python -m venv env
.\env\Scripts\Activate.ps1

# Instalar las dependencias
pip install -r requirements.txt
pip install pyinstaller

