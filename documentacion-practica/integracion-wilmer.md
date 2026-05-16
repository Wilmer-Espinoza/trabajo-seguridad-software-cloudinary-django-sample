# Integración continua - Wilmer

## Responsable

ESPINOZA OLVERA WILMER JOSUE

## Herramienta utilizada

La herramienta utilizada para la integración continua fue GitHub Actions, debido a que permite automatizar procesos dentro del repositorio y ejecutar validaciones cada vez que se realizan cambios en el proyecto.

## Archivo del pipeline

El archivo de configuración del pipeline fue creado en la siguiente ruta:

.github/workflows/django-ci.yml

## Configuración del pipeline

```yaml
name: Django CI

on:
  push:
    branches: [ "master", "integracion-wilmer" ]
  pull_request:
    branches: [ "master" ]

jobs:
  build:
    runs-on: ubuntu-latest

    env:
      CLOUDINARY_CLOUD_NAME: demo
      CLOUDINARY_API_KEY: 123456789
      CLOUDINARY_API_SECRET: 123456789
      SECRET_KEY: github-actions-secret-key
      DEBUG: "False"

    steps:
      - name: Descargar el código del repositorio
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Verificar estructura del proyecto Django
        run: |
          python manage.py check
