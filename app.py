import os

def get_android_data_directories(root_path='/storage/emulated/0'):
    # Diccionario para almacenar rutas de datos específicos
    data_directories = {
        'Images': [],
        'Videos': [],
        'Documents': [],
        'Downloads': [],
        'Music': [],
        'Contacts': [],
        'AppData': []
    }
    
    # Recorrer las carpetas comunes de Android
    for root, dirs, files in os.walk(root_path):
        # Imágenes y fotos
        if 'DCIM' in root or 'Pictures' in root:
            data_directories['Images'].append(root)
        # Videos
        elif 'Movies' in root or 'Videos' in root:
            data_directories['Videos'].append(root)
        # Documentos y descargas
        elif 'Documents' in root:
            data_directories['Documents'].append(root)
        elif 'Download' in root:
            data_directories['Downloads'].append(root)
        # Música
        elif 'Music' in root:
            data_directories['Music'].append(root)
        # Contactos y otros datos de aplicaciones
        elif 'contacts' in root.lower():
            data_directories['Contacts'].append(root)
        elif 'Android/data' in root or 'Android/obb' in root:
            data_directories['AppData'].append(root)
    
    # Mostrar los directorios encontrados
    for category, paths in data_directories.items():
        print(f"\n{category} Directories:")
        for path in paths:
            print(f"  - {path}")

# Ejecutar el script
get_android_data_directories()
