#!/usr/bin/env python3
import os

# Crear entorno virtual
os.system("python -m venv .venv")

# Activar entorno virtual
if os.name == 'nt':
    venv_activate = ".venv\Scripts\activate.bat"
else:
    venv_activate = ".venv/bin/activate"
    os.system(f"source {venv_activate}")

# Instalar dependencias
os.system("python -m pip install -r requirements.txt")

# Crear migraciones y aplicarlas
os.system("python manage.py makemigrations")
os.system("python manage.py migrate")

# Cargar datos a la base de datos
os.system("python manage.py loaddata hotel_data.json")

# Correr el servidor web
os.system("python manage.py runserver")
