import sys
sys.path.append( "src" )

import psycopg2

from model.CipherEngine import CipherEngine
from model.CipherError import EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError, WrongInfoError, UsedKeyError
import SecretConfig

class EncryptionController:

    def CreateTable():
        """ Crea la tabla de textos encriptados en la Base de Datos """
        try: 
            cursor = EncryptionController.GetCursor()
            cursor.execute("create table cipher (key VARCHAR(20) PRIMARY KEY NOT NULL, encrypt_text TEXT NOT NULL);")
            cursor.connection.commit()
        except:
            cursor.connection.rollback()

    def DeleteTable():
        """ Borra la tabla en su totalidad """    
        cursor = EncryptionController.GetCursor()
        cursor.execute( "drop table cipher;" )
        cursor.connection.commit()

    def InsertIntoTableEncrypt(text_to_encrypt: str, key: str):
        """ Insertar datos requeridos por el usuario"""
        if not text_to_encrypt:
            raise EmptyTextError("El texto a encriptar está vacío.")

        if not key:
            raise EmptyKeyError("La llave de encriptación está vacía.")

        for character in key:
            if not character.isalnum():
                raise KeyCharacterError("La clave de encriptación contiene caracteres no válidos o especiales.")

        if len(text_to_encrypt) < len(key):
            raise LongerKeyError("La clave es más larga que el texto a encriptar.")
        
        try:           
            encrypted_text = CipherEngine.EncryptText(text_to_encrypt, key)

            cursor = EncryptionController.GetCursor()
            cursor.execute(f"SELECT COUNT(*) FROM cipher WHERE key = '{key}';")
            count = cursor.fetchone()[0]
            if count > 0:
                raise UsedKeyError("La clave ya está en uso.")
            
            cursor.execute(f"""
            insert into cipher (key, encrypt_text)
            values ('{key}', '{encrypted_text}');
            """)
            cursor.connection.commit()
            return encrypted_text
        except:
            cursor.connection.rollback() 
            raise Exception("No fue posible insertar")
        
    def GetEncryptText(key: str, encrypted_text: str):
        if not encrypted_text:
            raise EmptyTextError("El texto a desencriptar está vacío.")

        if not key:
            raise EmptyKeyError("La llave de desencriptación está vacía.")

        for character in key:
            if not character.isalnum():
                raise KeyCharacterError("La clave de encriptación contiene caracteres no válidos o especiales.")

        if len(encrypted_text) < len(key):
            raise LongerKeyError("La clave es más larga que el texto a desencriptar.")
        
        try:
            cursor = EncryptionController.GetCursor()
            cursor.execute(f"""select encrypt_text from cipher where key = '{key}' and encrypt_text = '{encrypted_text}'""")
            record = cursor.fetchone()
            if record:
                return record[0]
        except:
            cursor.connection.rollback()
            raise Exception("No hay un registro con estos datos.")

    def DecryptText(key: str, encrypted_text: str):
        """ Desencriptar texto utilizando la clave y el texto encriptado """
        if not encrypted_text:
            raise EmptyTextError("El texto a desencriptar está vacío.")

        if not key:
            raise EmptyKeyError("La llave de desencriptación está vacía.")

        for character in key:
            if not character.isalnum():
                raise KeyCharacterError("La clave de encriptación contiene caracteres no válidos o especiales.")

        if len(encrypted_text) < len(key):
            raise LongerKeyError("La clave es más larga que el texto a desencriptar.")

        try:
            cursor = EncryptionController.GetCursor()
            cursor.execute(f"""select encrypt_text from cipher where key = '{key}' and encrypt_text = '{encrypted_text}'""")
            decrypted_data = cursor.fetchone()
            if decrypted_data:
                database_encrypted_text = decrypted_data[0]
                return CipherEngine.DecryptText(database_encrypted_text, key)
            else:
                raise WrongInfoError("No se encontraron datos en la base de datos para la clave y el texto encriptado proporcionados.")
        except:
            cursor.connection.rollback()
            raise WrongInfoError("No se encontraron datos en la base de datos para la clave y el texto encriptado proporcionados.")
        
    def DeleteFromTable(key: str, encrypted_text: str):
        """ Elimina registros de la tabla según la clave y el texto encriptado proporcionados por el usuario """

        if not encrypted_text:
            raise EmptyTextError("El texto a desencriptar está vacío.")

        if not key:
            raise EmptyKeyError("La llave de desencriptación está vacía.")

        for character in key:
            if not character.isalnum():
                raise KeyCharacterError("La clave de encriptación contiene caracteres no válidos o especiales.")

        if len(encrypted_text) < len(key):
            raise LongerKeyError("La clave es más larga que el texto a desencriptar.")

        try:
            cursor = EncryptionController.GetCursor()
            cursor.execute(f""" select key, encrypt_text from cipher where key = '{key}' and encrypt_text = '{encrypted_text}';""")
            existing_record = cursor.fetchone()
            if existing_record:
                cursor.execute(f"""delete from cipher where key = '{key}' and encrypt_text = '{encrypted_text}';""")
                cursor.connection.commit()
            else:
                raise WrongInfoError("No se encontraron datos en la base de datos para la clave y el texto encriptado proporcionados.")
        except:
            cursor.connection.rollback()
            raise Exception("No fue posible eliminar el registro.")
        

    def UpdateFromTable(key: str, encrypted_text: str, new_text: str):
        """ Actualiza el contenido del texto encriptado dejando la misma clave """
        if not encrypted_text:
            raise EmptyTextError("El texto a desencriptar está vacío.")

        if not key:
            raise EmptyKeyError("La llave de desencriptación está vacía.")
        
        if not new_text:
            raise EmptyTextError("El nuevo texto está vacío.")

        for character in key:
            if not character.isalnum():
                raise KeyCharacterError("La clave de encriptación contiene caracteres no válidos o especiales.")

        if len(encrypted_text) < len(key):
            raise LongerKeyError("La clave es más larga que el texto a desencriptar.")
        
        if len(new_text) < len(key):
            raise LongerKeyError("La clave es más larga que el nuevo texto.")
        
        
        try:
            new_encrypted_text = CipherEngine.EncryptText(new_text, key)
            cursor = EncryptionController.GetCursor()
            cursor.execute(f"""update cipher set encrypt_text = '{new_encrypted_text}' where key = '{key}' and encrypt_text = '{encrypted_text}';""")
            cursor.connection.commit()            
            return new_encrypted_text
        except Exception as e:
            cursor.connection.rollback()
            raise Exception("No fue posible actualizar el texto encriptado:", e)


    def GetCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        cursor = connection.cursor()
        return cursor