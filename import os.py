import os
from PIL import Image

def verificar_imagenes(ruta):
    for carpeta, subcarpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            try:
                ruta_completa = os.path.join(carpeta, archivo)
                with Image.open(ruta_completa) as img:
                    img.verify()  # Verificar si la imagen es válida
            except (IOError, SyntaxError):
                print(f"Imagen corrupta: {ruta_completa}")

# Cambia 'ruta_train' y 'ruta_valid' por las carpetas de imágenes
verificar_imagenes('C:/Users/JCM/Desktop/final_inteligente/train/images')
verificar_imagenes('C:/Users/JCM/Desktop/final_inteligente/valid/images')
