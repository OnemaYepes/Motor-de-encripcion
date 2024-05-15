"""
Interfaz de usuario por consola

"""
import sys
sys.path.append("src")
from model.CipherError import EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError, WrongInfoError
from controller.EncryptionController import EncryptionController

class ConsoleUI:
    @staticmethod
    def EncryptText():
        try:
            text = input("Ingrese el texto a encriptar: ")
            key = input("Ingrese la clave de encriptación: ")
            encrypted_text = EncryptionController.InsertIntoTableEncrypt(text, key)
            print("El mensaje encriptado es ->", encrypted_text)
        except (EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError) as e:
            print("Error:", e)
        except Exception as e:
            print("Error inesperado:", e)

    @staticmethod
    def DecryptText():
        try:
            encrypted_text = input("Ingrese el texto encriptado: ")
            key = input("Ingrese la clave de desencriptación: ")
            decrypt_text = EncryptionController.DecryptText(key, encrypted_text)
            print("El mensaje original es ->", decrypt_text)
        except (EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError, WrongInfoError) as e:
            print("Error:", e)
        except Exception as e:
            print("Error inesperado:", e)
    
    @staticmethod
    def DeleteRegister():
        try:
            encrypted_text = input("Ingrese el texto encriptado: ")
            key = input("Ingrese la clave de desencriptación: ")
            print("Eliminando...")
            EncryptionController.DeleteFromTable(key, encrypted_text)
            print("Registros eliminados exitosamente.")
        except (EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError, WrongInfoError) as e:
            print("Error:", e)
        except Exception as e:
            print("Error inesperado:", e)
            
    @staticmethod
    def UpdateRegister():
        try:
            encrypted_text = input("Ingrese el texto encriptado: ")
            key = input("Ingrese la clave de desencriptación: ")
            new_text = input("Ingrese el nuevo texto que desea encriptar: ")
            new_encrypted_text = EncryptionController.UpdateFromTable(key, encrypted_text, new_text)
            print(f"El nuevo texto '{new_text}' con clave '{key}' encriptado, es:\n->  {new_encrypted_text}")
        except (EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError, WrongInfoError) as e:
            print("Error:", e)
        except Exception as e:
            print("Error inesperado:", e)

    @staticmethod
    def DisplayMenu():
        print("Seleccione una opción:\n")
        print("1. Encriptar texto")
        print("2. Desencriptar texto")
        print("3. Eliminar registro")
        print("4. Para actualizar el mensaje encriptado")
        print("5. Salir")

    @classmethod
    def main(cls):
        while True:
            cls.DisplayMenu()
            choice = input("\nOpción: ")
            EncryptionController.CreateTable()
            if choice == "1":
                cls.EncryptText()
            elif choice == "2":
                cls.DecryptText()
            elif choice == "3":
                cls.DeleteRegister()
            elif choice == "4":
                cls.UpdateRegister()
            elif choice == "5":
                print("Saliendo...")
                borrar = input("¿Deseas borrar la tabla? (Y/N): ")
                if borrar == "Y":
                    EncryptionController.DeleteTable()
                    break
                else:
                    break
            else:
                print("\nOpción no válida. Intente de nuevo.")

if __name__ == "__main__":
    ConsoleUI.main()