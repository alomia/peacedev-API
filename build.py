#!/usr/bin/python3
import os
import platform

# Crear entorno virtual
if platform.system() == "Windows":
    os.system("python -m venv .venv")
    venv_activate = ".venv/Scripts/activate"
else:
    os.system("python3 -m venv .venv")
    venv_activate = ".venv/bin/activate"

# Activar entorno virtual
os.system(f"source {venv_activate}")

# Instalar dependencias
os.system("pip install -r requirements.txt")

# Crear migraciones y aplicarlas
os.system("python manage.py makemigrations")
os.system("python manage.py migrate")

# Cargar datos a la base de datos
os.system("python manage.py loaddata hotel_data.json")

# Correr el servidor web
os.system("python manage.py runserver")
