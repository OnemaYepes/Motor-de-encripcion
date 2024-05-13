import sys
sys.path.append( "src" )

import psycopg2

from model.CipherEngine import CipherEngine
import SecretConfig

class EncryptionController:

    def CreateTable():
        """ Crea la tabla de textos encriptados en la Base de Datos """
        try: 
            cursor = EncryptionController.GetCursor()
            cursor.execute("create table cipher (key VARCHAR(20) PRIMARY KEY NOT NULL, text TEXT NOT NULL, encrypt_text TEXT NOT NULL);")
            cursor.connection.commit()
        except:
            cursor.connection.rollback()

    def DeleteTable():
        """ Borra la tabla en su totalidad """    
        cursor = EncryptionController.GetCursor()
        cursor.execute( "drop table cipher;" )
        cursor.connection.commit()

    def InsertIntoTable(text_to_encrypt: str, key: str):
        """ Insertar datos requeridos por el usuario"""
        try:
            encrypted_text = CipherEngine.EncryptText(text_to_encrypt, key)

            cursor = EncryptionController.GetCursor()
            cursor.execute(f"""
            insert into cipher (key,   text,  encrypt_text)
            values ('{key}',  '{text_to_encrypt}', '{encrypted_text}');
            """)

            cursor.connection.commit()
        except:
            cursor.connection.rollback() 
            raise Exception("No fue posible insertar")
        
    def SearchInTable(encrypted_text: str, key: str):
        """ Buscar según texto encriptado y su clave """
        try:
            cursor = EncryptionController.GetCursor()
            cursor.execute(f"""select key,   text,  encrypt_text from cipher where key = '{key}' and encrypt_text = '{encrypted_text}'""")
            decrypt = cursor.fetchone()
            return print("El mensaje original es: ", decrypt[1])
        except:
            cursor.connection.rollback()
            raise Exception("No fue posible desencriptar")



    def GetCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor