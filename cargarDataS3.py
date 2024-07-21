import boto3
import datetime

def guardar_datos_crudos_s3(nombre_bucket, ruta_carpeta_s3, nombre_archivo):
    # Crear una instancia de cliente de S3
    s3 = boto3.client('s3')
    
    try:
        # Subir el archivo CSV al bucket
        s3.upload_file(nombre_archivo, nombre_bucket, f"{ruta_carpeta_s3}/{nombre_archivo.split('/')[-1]}")
        print(f"Archivo {nombre_archivo} subido exitosamente a s3://{nombre_bucket}/{ruta_carpeta_s3}/")
    except Exception as e:
        print(f"Error al subir el archivo a S3: {e}")

# Fecha actual
hoy = datetime.date.today()

# Nombre del bucket
nombre_bucket = 'mi-datalake'

# Ruta de carpeta s3
ruta_s3 = f"datos_crudos/año={hoy.year}/mes={hoy.month}/dia={hoy.day}"

# Ruta local de archivo
archivo_csv = "" #Especificar Ruta

# Llamar a la función para subir el archivo
guardar_datos_crudos_s3(nombre_bucket, ruta_s3, archivo_csv)
