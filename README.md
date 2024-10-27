# android-dumper
# Android Data Directories Scanner

Este proyecto es un script en Python que identifica y lista los principales directorios en un dispositivo Android donde se suelen almacenar datos, como imágenes, videos, documentos, música, contactos, y datos de aplicaciones. 

El script recorre el sistema de archivos de Android y organiza los directorios en categorías para facilitar su identificación y gestión.

## Características

- Identifica los directorios donde se guardan fotos e imágenes, como la carpeta **DCIM** y **Pictures**.
- Localiza carpetas para videos (**Movies** y **Videos**).
- Encuentra directorios de documentos y descargas como **Documents** y **Download**.
- Identifica carpetas de música y audio en **Music**.
- Escanea en busca de directorios de contactos y datos específicos de aplicaciones, como **Android/data** y **Android/obb**.
- Muestra en consola los resultados categorizados y organizados para una lectura rápida.

## Requisitos

- **Python 3.x** debe estar instalado en tu sistema.
- Este script está diseñado para ejecutarse en un dispositivo Android o en un entorno donde el almacenamiento de Android esté montado y accesible (por ejemplo, usando `adb pull` en una computadora con el almacenamiento del dispositivo Android).

## Uso

1. **Clonar este repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/android-data-directories-scanner.git
   cd android-data-directories-scanner
