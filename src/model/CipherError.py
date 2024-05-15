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

class WrongInfoError(Exception):
    """
    Raised when the key or the encrypted text doesn't match the datatable.
    
    Se ejecuta cuando la clave o el texto encriptado no se encuentran en la tabla
    
    """
    pass

class UsedKeyError(Exception):
    """
    Raised when the key is already taken.
    
    Se ejecuta cuando la clave ya está en uso.
    
    """
    pass