
# Rick and Morty App

## Descripción

Esta aplicación es una interfaz gráfica de usuario (GUI) basada en Python y Tkinter que permite a los usuarios buscar y visualizar personajes de la serie "Rick and Morty". La aplicación utiliza la API pública de Rick and Morty para obtener los datos de los personajes.

## Requisitos

- Python 3.8+
- Tkinter
- Pillow
- Requests
- PyInstaller (para la compilación a .exe)

## Instalación y Configuración del Entorno

### Habilitar la Ejecución de Scripts en PowerShell

**Nota: Habilitar la ejecución de scripts en PowerShell puede tener implicaciones de seguridad. Asegúrate de que entiendes los riesgos y solo habilita esta opción si estás seguro de hacerlo.**

1. Abre PowerShell como administrador.
2. Ejecuta el siguiente comando para verificar la política de ejecución actual:

    ```sh
    Get-ExecutionPolicy
    ```

3. Si la política de ejecución es `Restricted`, cambia la política a `RemoteSigned` para permitir la ejecución de scripts locales firmados:

    ```sh
    Set-ExecutionPolicy RemoteSigned
    ```

4. Confirma el cambio cuando se te solicite.

5. Después de ejecutar los scripts necesarios, puedes restablecer la política de ejecución a `Restricted` para mejorar la seguridad:

    ```sh
    Set-ExecutionPolicy Restricted
    ```

### Instalación del Proyecto

1. Clonar el repositorio en tu máquina local:

    ```sh
    git clone https://github.com/Naofumi-Alu/PythonApp-Api-Practice.git
    cd rick-and-morty-app
    ```

2. Ejecutar el script de configuración para crear y activar el entorno virtual, instalar las dependencias y compilar la aplicación:

    ```sh
    .\setup.ps1
    ```

## Compilación a .exe

Para compilar la aplicación a un ejecutable (.exe) usando PyInstaller, sigue estos pasos:

1. Ejecuta el script de compilación:

    ```sh
    .\setup.ps1
    ```

2. El ejecutable compilado se encontrará en la carpeta `dist`.

## Modificación del Archivo main.spec

Si necesitas personalizar la configuración de la compilación, puedes modificar el archivo `main.spec` según tus necesidades. Este archivo contiene las especificaciones que PyInstaller usa para construir el ejecutable.

## Estructura del Proyecto

- `main.py`: Archivo principal que inicia la aplicación.
- `src/`
  - `gui.py`: Maneja la lógica de la pantalla de inicio y el inicio de sesión.
  - `main_screen.py`: Maneja la lógica de la pantalla principal y la visualización de los personajes.
  - `api.py`: Contiene funciones para interactuar con la API de Rick and Morty.
  - `utils.py`: Funciones auxiliares como el manejo de errores.
- `assets/images/`: Carpeta donde se guardan las imágenes de los personajes.
- `tests/`: Contiene las pruebas unitarias (No disponible en este release)
- `logs/`: Contiene los logs de las pruebas unitarias (No disponible en este release)

## Depuración

Para depurar el proyecto, puedes usar las herramientas integradas en tu IDE favorito como Visual Studio Code, PyCharm, entre otros. También puedes agregar `print` statements o usar el módulo `pdb` de Python para depuración paso a paso.

1. Ejecuta el script en modo interactivo:

    ```sh
    python -m pdb main.py
    ```

2. Coloca puntos de interrupción (`breakpoints`) en tu código donde desees detener la ejecución y analizar el estado del programa.

## Credenciales de ejecución

Las credenciales son sensibles a las Mayusculas, por lo que deberá revisar muy bien las credenciales a ingresar

1. Username: admin
2. Password: admin


## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature-nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agregar nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature-nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Agradecimientos

Gracias a la API pública de Rick and Morty por proporcionar los datos de los personajes.
