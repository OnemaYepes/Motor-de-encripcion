"""
Interfaz de usuario por consola

"""
import sys
sys.path.append("src")
from CipherEngine.CipherEngine import CipherEngine, EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError

class ConsoleUI:
    @staticmethod
    def EncryptText():
        try:
            text = input("Ingrese el texto a encriptar: ")
            key = input("Ingrese la clave de encriptación: ")
            encrypted_text = CipherEngine.EncryptText(text, key)
            print(f"Texto encriptado:\n{encrypted_text}")
        except (EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError) as e:
            print("Error:", e)
        except Exception as e:
            print("Error inesperado:", e)

    @staticmethod
    def DecryptText():
        try:
            encrypted_text = input("Ingrese el texto encriptado: ")
            key = input("Ingrese la clave de desencriptación: ")
            decrypted_text = CipherEngine.DecryptText(encrypted_text, key)
            print(f"Texto desencriptado:\n{decrypted_text}")
        except (EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError) as e:
            print("Error:", e)
        except Exception as e:
            print("Error inesperado:", e)

    @staticmethod
    def DisplayMenu():
        print("Seleccione una opción:")
        print("1. Encriptar texto")
        print("2. Desencriptar texto")
        print("3. Salir")

    @classmethod
    def main(cls):
        while True:
            cls.DisplayMenu()
            choice = input("Opción: ")

            if choice == "1":
                cls.EncryptText()
            elif choice == "2":
                cls.DecryptText()
            elif choice == "3":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    ConsoleUI.main()