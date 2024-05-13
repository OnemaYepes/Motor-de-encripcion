#Impotación para modificar texto
import codecs

class EmptyTextError(Exception):
    """
    Raised when the text to be encrypted or decrypted is empty. 

    Se ejecuta cuando el texto a encriptar o desencriptar está vacío.

    """
    pass

class EmptyKeyError(Exception):
    """
    Raised when the encryption or decryption key is empty.
    
    Se ejecuta cuando la llave para encriptar o desencriptar está vacía.

    """
    pass

class KeyCharacterError(Exception):
    """
    Raised when the encryption or decryption key contain at least one special character.
    
    Se ejecuta cuando la clave de encriptación o desencriptación contiene al menos un caracter especial.

    """
    pass

class LongerKeyError(Exception):
    """
    Raised when the key is longer than the text to encrypt or decrypt.
    
    Se ejecuta cuando la clave es más larga que el texto a encriptar o desencriptar.
    
    """
    pass

class CipherEngine:
    """
    Class that runs the encryption and decryption engine.

    Clase que ejecuta el motor de encripción y desencriptación.
    """

    def EncryptText(text_to_encrypt: str, key: str) -> str:
        """
        Encrypts a given text using a provided encryption key.

        Encripta un texto dado, usando una clave de encripción.

        Args:
            text_to_encrypt (str): The text to be encrypted.
            key (str): The encryption key.

        Raises:
            EmptyTextError: If the text is empty.
            EmptyKeyError: If the encryption key is empty.
            KeyCharacterError: If the encryption key contains invalid characters.
            LongerKeyError: If the encryption key is longer than the text to be encrypted.
        
        Returns:
            encrypted_text (str): The encrypted text.
        """

        if not text_to_encrypt:
            raise EmptyTextError("El texto a encriptar está vacío.")

        if not key:
            raise EmptyKeyError("La llave de encriptación está vacía.")

        for character in key:
            if not character.isalnum():
                raise KeyCharacterError("La clave de encriptación contiene caracteres no válidos o especiales.")

        if len(text_to_encrypt) < len(key):
            raise LongerKeyError("La clave es más larga que el texto a encriptar.")


        encrypted_text = ""

        for index in range(len(text_to_encrypt)):
            text = text_to_encrypt[index]
            key_to_encrypt = key[index%len(key)]

            encrypted_text += chr(ord(text) ^ ord(key_to_encrypt))
        
        encrypted_text = encrypted_text.encode('utf-8').hex()
        return encrypted_text

    def DecryptText(encrypted_text: str, key: str) -> str:
        """
        Decrypts an encrypted text using a provided decryption key.

        Descifra un texto encriptado utilizando una clave de descifrado proporcionada.


        Args:
            encrypted_text (str): The encrypted text.
            key (str): The decryption key.

        Raises:
            EmptyTextError: If the encrypted text is empty.
            EmptyKeyError: If the decryption key is empty.
            KeyCharacterError: If the decryption key contains invalid characters.
            LongerKeyError: If the decryption key is longer than the text to be encrypted.
        
        Returns:
            decrypted_text (str): The decrypted message.
        """

        if not encrypted_text:
            raise EmptyTextError("El texto a desencriptar está vacío.")

        if not key:
            raise EmptyKeyError("La llave de desencriptación está vacía.")

        for character in key:
            if not character.isalnum():
                raise KeyCharacterError("La clave de encriptación contiene caracteres no válidos o especiales.")

        if len(encrypted_text) < len(key):
            raise LongerKeyError("La clave es más larga que el texto a desencriptar.")

        decrypted_text = ""
        encrypted_text = codecs.decode(encrypted_text, 'hex').decode('utf-8')

        for index in range(len(encrypted_text)):
            text = encrypted_text[index]
            key_to_decrypt = key[index%len(key)]

            decrypted_text += chr(ord(text) ^ ord(key_to_decrypt))

        return decrypted_text

