es

# Descripción del Script

Este script está diseñado para reparar imágenes y videos cuyas fechas de creación han sido alteradas, recuperando la fecha original a partir del nombre del archivo si es posible. Es útil cuando los archivos multimedia pierden su información de fecha y hora, lo que puede ocurrir durante la manipulación de archivos o la transferencia entre dispositivos.

El script realiza las siguientes acciones:

1. **Extracción de fechas**: Examina el nombre de los archivos para extraer la fecha de creación original.
2. **Actualización de fechas**: Utiliza la información extraída para restablecer la fecha de creación de los archivos multimedia.
3. **Copiado de archivos**: Copia los archivos procesados correctamente a una carpeta de salida llamada "output".
4. **Compresión de resultados**: Comprime la carpeta "output" en un archivo ZIP para facilitar su almacenamiento y distribución.

El proceso de reparación se lleva a cabo tanto para archivos de imagen como para archivos de video, garantizando la coherencia en la información de fecha y hora en todo tipo de archivos multimedia.

# Instrucciones de Uso

1. **Instalación de Dependencias**: Asegúrese de tener instaladas las siguientes dependencias antes de ejecutar el script:
   - `piexif`: Se utiliza para acceder y modificar los metadatos EXIF de las imágenes. Puede instalarlo ejecutando el siguiente comando:
     ```
     pip install piexif
     ```
   - `zipfile`: Se utiliza para comprimir la carpeta de salida en un archivo ZIP.
     ```
     pip install zipfile
     ```

2. **Ejecución del Script**: Para ejecutar el script, simplemente ejecute el archivo Python en el directorio que contiene los archivos multimedia que desea reparar.

3. **Revisión de Resultados**: Después de la ejecución, revise la salida del script para verificar los archivos procesados correctamente y cualquier error que pueda haber ocurrido durante el proceso de reparación.

# Consideraciones Importantes

- Asegúrese de que los archivos multimedia estén ubicados en el mismo directorio que el script antes de ejecutarlo.
- Es posible que algunos archivos no puedan ser reparados si la información de fecha original no está presente en el nombre del archivo.
- Revise la carpeta "output" después de la ejecución para acceder a los archivos reparados y comprimidos.

en

# Script Description

This script is designed to repair images and videos whose creation dates have been altered, recovering the original date from the filename if possible. It's useful when multimedia files lose their date and time information, which can happen during file manipulation or transfer between devices.

The script performs the following actions:

1. **Date Extraction**: It examines the filenames to extract the original creation date.
2. **Date Update**: It uses the extracted information to reset the creation date of multimedia files.
3. **File Copying**: It copies the successfully processed files to an output folder named "output".
4. **Result Compression**: It compresses the "output" folder into a ZIP file for easier storage and distribution.

The repair process is carried out for both image and video files, ensuring consistency in date and time information across all types of multimedia files.

# Usage Instructions

1. **Dependency Installation**: Ensure the following dependencies are installed before running the script:
   - `piexif`: Used to access and modify EXIF metadata of images. You can install it by running the following command:
     ```
     pip install piexif
     ```
   - `zipfile`: Used to compress the output folder into a ZIP file. You can install it by running the following command:
     ```
     pip install zipfile
     ```

2. **Running the Script**: To execute the script, simply run the Python file in the directory containing the multimedia files you want to repair.

3. **Reviewing Results**: After execution, review the script output to verify the files processed successfully and any errors that may have occurred during the repair process.

# Important Considerations

- Ensure that multimedia files are located in the same directory as the script before executing it.
- Some files may not be repairable if the original date information is not present in the filename.
- Review the "output" folder after execution to access the repaired and compressed files.