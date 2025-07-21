[![Lang en](https://img.shields.io/badge/lang-en-blue?style=flat)](https://github.com/ian-ani/diff_files/blob/main/README.md)
[![Lang es](https://img.shields.io/badge/lang-es-red?style=flat)](https://github.com/ian-ani/diff_files/blob/main/README.es.md)

## Tabla de contenidos

- [Acerca de este repositorio](#Acerca-de-este-repositorio)
- [Librerías utilizadas](#Librerías-utilizadas)
- [Uso](#Uso)

## Acerca de este repositorio

Programa creado con **Python** para la comprobación de dos archivos de texto.
Probado con Windows 10.

## Hecho con

- os
- tkinter
- json
- difflib

## Uso

1. Lanzar **main.py**.
2. Hacer clic en **First file** para añadir un primer archivo a comprobar.
3. Hacer clic en **Second file** para añadir un segundo archivo a comprobar.
4. Hacer clic en **Save** para elegir donde guardar el archivo, si no se proporciona ninguna ruta 
por defecto creará un directorio con el nombre de **output** y un archivo con el nombre **diff.html**.
5. Hacer clic en **Run** para que se haga la comprobación de ambos archivos y sus diferencias.
6. Comprobar el archivo HTML de reporte.

### Funciona con

Cualquier archivo de texto plano como: .py, .txt, .json (cuadernos de Jupyter incluidos), .css, .html.

### No funciona con

Cualquier archivo que no sea de texto plano como: imágenes, vídeos, archivos de Word, archivos de Excel.
