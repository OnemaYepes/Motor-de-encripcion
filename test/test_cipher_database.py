# Todas las prueba sunitarias importan la biblioteca unittest
import unittest

import sys
sys.path.append("src")

from datetime import date

from controller.EncryptionController import EncryptionController
from model.CipherError import EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError


import psycopg2

class ControllerTest(unittest.TestCase):

    # Test Fixture
    def setUpClass():
        # Llamar a la clase Controlador para que cree la tabla
        EncryptionController.DeleteTable()
        EncryptionController.CreateTable()

    def test_correct_DB_encryption(self):
        """ Prueba que se cree correctamente la tabla en la BD """
        text_to_encrypt = "Emily and Harry were sitting in the park"
        key = "258"
        expected_encrypted_text = "7758515e4c18535b5c127d5940474112425d405018415c4c465c565515515c154c5a501842544a59"
        EncryptionController.InsertIntoTableEncrypt(text_to_encrypt, key)

        search_record = EncryptionController.GetEncryptText(key, expected_encrypted_text)

        self.assertEqual(search_record, expected_encrypted_text)

    def test_empty_key( self ):
        """ Prueba de clave vacía """
        text_to_encrypt = "Mañana te espero detrás de la fuente"
        key = None
        self.assertRaises( EmptyKeyError, EncryptionController.InsertIntoTableEncrypt, text_to_encrypt, key )

    def test_correct_DB_decrypt(self):
        """ Prueba de desencriptar correcta """
        encrypted_text = "7e5c4b10565b5c42464c51515b435740185e5a145953505d5e15585e12424d5515415f5d1349455c5143571f18435c5a5e125f57104441541246565f15585441135c595651"
        key = "2380541"

        og_text = "Los computadores no hacen lo que uno quiere, sino lo que uno les dice"
        EncryptionController.InsertIntoTableEncrypt(og_text, key)

        decrypted_text = EncryptionController.DecryptText(key, encrypted_text)

        self.assertEqual(og_text, decrypted_text)

    def test_unexisting_key(self):
        """ Prueba con clave no registrada """
        encrypted_text = "614044575353"
        key = "12"
        og_text = "Prueba"
        fake_key = "3312"
        EncryptionController.InsertIntoTableEncrypt(og_text, key)

        self.assertRaises( Exception, EncryptionController.DecryptText, fake_key, encrypted_text)

    def test_delete_record(self):
        """ Prueba para eliminar un registro """
        text_to_encrypt = "Emily and Harry were sitting in the park"
        key = "258"
        encrypted_text = "7758515e4c18535b5c127d5940474112425d405018415c4c465c565515515c154c5a501842544a59"
        EncryptionController.InsertIntoTableEncrypt(text_to_encrypt, key)

        EncryptionController.DeleteFromTable(key, encrypted_text)

        result = EncryptionController.GetEncryptText('258', 'encrypted_text')
        self.assertEqual(result, None)

    def test_wrong_encrypted_text(self):
        """ Prueba cuando se da un texto encriptado incorrecto """
        fake_encrypted_text = "1519524019074553024788515110"
        key = "pw12"
        og_text = "encriptar"
        EncryptionController.InsertIntoTableEncrypt(og_text, key)

        self.assertRaises( Exception, EncryptionController.DeleteFromTable, key, fake_encrypted_text)

    def test_update_text(self):
        """ Prueba de actualizar el texto encriptado de un registro dejando la misma clave """
        text_to_encrypt = "3.14159265359"
        encrypted_text = "6347615d615c695b665c635c69"
        key = "Pi"
        new_text = "Ciento Ochenta Grados"
        excepted_new_encrypted_text = "1300350724067026330135072408702e2208340623"

        EncryptionController.InsertIntoTableEncrypt(text_to_encrypt, key)

        new_encrypted_text = EncryptionController.UpdateFromTable(key, encrypted_text, new_text)
        self.assertEqual(excepted_new_encrypted_text, new_encrypted_text)

    def test_shorter_new_text(self):
        """ Prueba cuando el nuevo texto es más corto que la clave """
        text_to_encrypt = "Que linda rosa tienes"
        encrypted_text = "241b154f09040f140052131b1a144e040600030403"
        key = "unpoemaparati"
        new_text = "Girasol"

        EncryptionController.InsertIntoTableEncrypt(text_to_encrypt, key)

        self.assertRaises( Exception, EncryptionController.UpdateFromTable, key, encrypted_text, new_text)


if __name__ == '__main__':
    unittest.main()