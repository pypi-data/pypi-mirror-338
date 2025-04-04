import pandas as pd
import psycopg2
from psycopg2 import OperationalError, errorcodes
import smtplib

def connectDB(host, database, user, password, port):
    try:
        # Crea una conexión de Redshift
        conn = psycopg2.connect(
            host=host,
            database=database,
            port=port,
            user=user,
            password=password
        )
        print("Conexión exitosa a la base de datos.")
        return conn, conn.cursor()
    except OperationalError as e:
        # Manejo de errores específicos
        if e.pgcode == errorcodes.INVALID_PASSWORD:
            print("Contraseña inválida.")
        elif e.pgcode == errorcodes.INVALID_CATALOG_NAME:
            print("Base de datos no encontrada.")
        elif e.pgcode == errorcodes.CONNECTION_FAILURE:
            print("Error de conexión.")
        else:
            print(f"Error al conectar a la base de datos: {e}.")
        return None, None
    
def close_connect(conn, cursor):
    try:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
            print("Conexión cerrada.")
    except OperationalError as e:
        print(f"Error al cerrar la conexión: {e}.")

def querySQL(conn, query):
    
    #Ejecuta una consulta SQL y devuelve los resultados.
    try:
        df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}.")
        return None

def send_mail(sender_email, sender_password, recipient_emails, msg):
    # Config smtp
    smtp_server = 'smtp.office365.com'
    smtp_port = 587
    
    try:
        # Iniciar conexión con el servidor SMTP y enviar el correo
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_emails, msg.as_string())
        print("Correo electrónico enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}.")
    finally:
        try:
            # Cierra la conexión con el servidor SMTP
            server.quit()
        except NameError:
            pass  # Si 'server' no está definido, no hay nada que cerrar


def close_connect_SFTP(sftp, transport):
    
    try:
        sftp.close()
        transport.close()
        print("Conexión SFTP cerrada.")
        
    except Exception as e:
        print(f'Error cerrando la conexión: {e}.')

def ReadFile_SFTP(sftp, sftp_remote_file_path):
    
    try:
        #Lee archivo en memoria
        with sftp.file(sftp_remote_file_path, 'rb') as remote_file:
                file_data = BytesIO(remote_file.read())
                print(f"Archivo leído en memoria desde {sftp_remote_file_path}.")
        return file_data

    except Exception as e:
        print(f'Error leyendo archivo desde {sftp_remote_file_path}: {e}.')

def MoveFile(sftp, sftp_remote_file_path, sftp_target_directory,file):
    
    #now = datetime.now()
    #dt_string = now.strftime("%d%m%Y_%H:%M:%S")
    
    #sftp_target_file_path = sftp_target_directory + '/' + dt_string + '_' + file
    sftp_target_file_path = sftp_target_directory + '/' + file
    # Mover archivo a la subcarpeta en el SFTP
    try:
        sftp.stat(sftp_target_directory)
        sftp.rename(sftp_remote_file_path, sftp_target_file_path)
        print(f"Archivo movido a {sftp_target_file_path}.")
        
    except FileNotFoundError:
        print(f"Directorio de destino no encontrado: {sftp_target_directory}.")
