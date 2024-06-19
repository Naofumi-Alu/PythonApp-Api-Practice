# build.ps1
# Este script  compila la aplicación a .exe usando el archivo de especificaciones de PyInstaller

# Crear el archivo de especificaciones
pyinstaller main.spec


# Compilar el archivo ejecutable
pyinstaller main.spec

Write-Output "La compilación está completa. El archivo ejecutable se encuentra en la carpeta 'dist'."
