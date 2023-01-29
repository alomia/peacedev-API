#!/bin/bash

# Crear entorno virtual
if [ "$(uname)" == "Darwin" ]; then
    python3 -m venv .venv
    venv_activate=".venv/bin/activate"
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    python3 -m venv .venv
    venv_activate=".venv/bin/activate"
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    python -m venv .venv
    venv_activate=".venv/Scripts/activate"
fi

# Activar entorno virtual
source $venv_activate

# Instalar dependencias
pip install -r requirements.txt

# Crear migraciones y aplicarlas
python manage.py makemigrations
python manage.py migrate

# Cargar datos a la base de datos
python manage.py loaddata hotel_data.json

# Correr el servidor web
python manage.py runserver
