import shutil
import os
import glob
import piexif
import zipfile
from datetime import datetime

def change_creation_date_image(filename, current_photo, total_photos):
    try:
        filename_basename = os.path.basename(filename)

        if filename_basename.startswith("IMG"): 
            date_str = filename_basename[4:12]
        elif filename_basename[0] == '2': 
            date_str = filename_basename[0:8]

        elif filename_basename.startswith("Screenshot_"): 
            filename_basename = filename_basename.replace("-", "")
            date_str = filename_basename[11:19]
            print(date_str)
        else:
            date_str = "" 

        print("-----------------------------------------------------------------")
        print("Procesando el archivo:", filename_basename)

        date = datetime.strptime(date_str, "%Y%m%d")
        date_with_time = date.replace(hour=12, minute=0, second=0)
        print("Fecha extraída del nombre del archivo:", date_with_time)

        exif_dict = piexif.load(filename)
        if piexif.ImageIFD.DateTime in exif_dict["0th"]:
            exif_dict["0th"][piexif.ImageIFD.DateTime] = date_with_time.strftime("%Y:%m:%d %H:%M:%S")
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, filename)
            os.utime(filename, (date_with_time.timestamp(), date_with_time.timestamp()))
            print("\033[92mFecha de creación cambiada exitosamente.\033[0m", f"{current_photo}/{total_photos}") 
            print("-----------------------------------------------------------------")
            return True 
        else:
            os.utime(filename, (date_with_time.timestamp(), date_with_time.timestamp()))
            print("\033[92mFecha de creación establecida usando el nombre del archivo.\033[0m", f"{current_photo}/{total_photos}") 
            print("-----------------------------------------------------------------")
            return True 
    except Exception as e:
        print("\033[91mError al intentar cambiar la fecha de creación:", str(e), "\033[0m") 
        print("-----------------------------------------------------------------")
        return False 

def change_creation_date_video(filename, current_photo, total_photos):
    try:
        filename_basename = os.path.basename(filename)

        if filename_basename.startswith("VID"): 
            date_str = filename_basename[4:12]
        elif filename_basename[0].isdigit(): 
            date_str = filename_basename[0:8]
        else:
            date_str = "" 

        print("-----------------------------------------------------------------")
        print("Procesando el archivo:", filename_basename)

        date = datetime.strptime(date_str, "%Y%m%d")
        date_with_time = date.replace(hour=12, minute=0, second=0)
        print("Fecha extraída del nombre del archivo:", date_with_time)

        os.utime(filename, (date_with_time.timestamp(), date_with_time.timestamp()))
        print("\033[92mFecha de creación establecida usando el nombre del archivo.\033[0m", f"{current_photo}/{total_photos}") 
        print("-----------------------------------------------------------------")
        return True 
    except Exception as e:
        print("\033[91mError al intentar cambiar la fecha de creación:", str(e), "\033[0m") 
        print("-----------------------------------------------------------------")
        return False 

def listar_archivos_multimedia_directorio_actual():
    directorio_actual = os.getcwd()
    archivos_imagen = []
    archivos_video = []
    archivos_procesados_correctamente = []
    errores = 0
    archivos_procesados = 0
    archivos_con_errores = []  # Lista para almacenar los nombres de archivos con errores

    for archivo in glob.glob(os.path.join(directorio_actual, "*.jpg")):
        nombre_archivo = os.path.basename(archivo)
        archivos_imagen.append(nombre_archivo)

    for archivo in glob.glob(os.path.join(directorio_actual, "*.jpeg")):
        nombre_archivo = os.path.basename(archivo)
        archivos_imagen.append(nombre_archivo)

    for archivo in glob.glob(os.path.join(directorio_actual, "*.mp4")):
        nombre_archivo = os.path.basename(archivo)
        archivos_video.append(nombre_archivo)

    archivos_imagen.sort()
    archivos_video.sort()

    carpeta_output = os.path.join(directorio_actual, "output")
    if not os.path.exists(carpeta_output):
        os.makedirs(carpeta_output)

    total_archivos_imagen = len(archivos_imagen)
    total_archivos_video = len(archivos_video)

    print("\033[34mArchivos de imagen encontrados:\033[0m\n") 
    for i, archivo in enumerate(archivos_imagen, start=1):
        print(f"{i}.", archivo)

    print("\n\033[34mArchivos de video encontrados:\033[0m\n") 
    for i, archivo in enumerate(archivos_video, start=1):
        print(f"{i}.", archivo)

    for i, archivo in enumerate(archivos_imagen, start=1):
        ruta_archivo = os.path.join(directorio_actual, archivo)
        if change_creation_date_image(ruta_archivo, i, total_archivos_imagen):
            archivos_procesados_correctamente.append(ruta_archivo)
            archivos_procesados += 1
        else:
            errores += 1
            archivos_con_errores.append(archivo)  # Agregar el nombre del archivo a la lista de errores

    for i, archivo in enumerate(archivos_video, start=1):
        ruta_archivo = os.path.join(directorio_actual, archivo)
        if change_creation_date_video(ruta_archivo, i, total_archivos_video):
            archivos_procesados_correctamente.append(ruta_archivo)
            archivos_procesados += 1
        else:
            errores += 1
            archivos_con_errores.append(archivo)  # Agregar el nombre del archivo a la lista de errores

    # Copiar solo los archivos procesados correctamente al directorio output
    for archivo in archivos_procesados_correctamente:
        ruta_destino = os.path.join(carpeta_output, os.path.basename(archivo))
        shutil.copy(archivo, ruta_destino)

    print(f"\n\033[92mArchivos procesados con éxito:\033[0m {archivos_procesados}")
    print(f"\033[91mErrores:\033[0m {errores}")
    print(f"\033[34mArchivos totales:\033[0m {total_archivos_imagen + total_archivos_video}")

    if len(archivos_con_errores) > 0:
            print("\n\033[91mArchivos con errores:\033[0m\n")
            for archivo_error in archivos_con_errores:
                print("\033[91m" + archivo_error + "\033[0m")
                
def comprimir_resultado():
    try:
        ruta_directorio_actual = os.path.abspath(os.path.dirname(__file__))

        with zipfile.ZipFile(os.path.join(ruta_directorio_actual, "output.zip"), 'w') as zipf:
            for root, dirs, files in os.walk("output"):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), "output"))
        print("-----------------------------------------------------------------")
        print("\033[92mCarpeta 'output' comprimida exitosamente.\033[0m") 
        print("-----------------------------------------------------------------")
    except Exception as e:
        print("-----------------------------------------------------------------")
        print("\033[91mError al comprimir la carpeta 'output':\033[0m", str(e))
        print("-----------------------------------------------------------------")

listar_archivos_multimedia_directorio_actual()

print(f"\033[34mComprimiendo carpeta...\033[0m")

comprimir_resultado()
