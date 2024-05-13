import unittest
import sys
sys.path.append("src")

from CipherEngine.CipherEngine import CipherEngine, EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError

class CipherTest( unittest.TestCase ):
    """
    Unit Tests for text encryption

    Pruebas unitarias para encriptar o desencriptar texto
    """

    def test_correct_encryption(self):
        """ Normal input text and key  """
        text_to_encrypt = "Prueba"
        key = "12"

        expected_encrypted_text = "614044575353"

        encrypted_text = CipherEngine.EncryptText(text_to_encrypt, key)

        self.assertEqual(encrypted_text, expected_encrypted_text)
     
    def test_correct_encryption2(self):
        """ Normal input text and key  """
        text_to_encrypt = "Emily and Harry were sitting in the park"
        key = "258"

        expected_encrypted_text = "7758515e4c18535b5c127d5940474112425d405018415c4c465c565515515c154c5a501842544a59"

        encrypted_text = CipherEngine.EncryptText(text_to_encrypt, key)

        self.assertEqual(encrypted_text, expected_encrypted_text)

    def test_correct_encryption3(self):
        """ Normal input text and key  """
        text_to_encrypt = "Los computadores no hacen lo que uno quiere, sino lo que uno les dice"
        key = "2380541"

        expected_encrypted_text = "7e5c4b10565b5c42464c51515b435740185e5a145953505d5e15585e12424d5515415f5d1349455c5143571f18435c5a5e125f57104441541246565f15585441135c595651"

        encrypted_text = CipherEngine.EncryptText(text_to_encrypt, key)

        self.assertEqual(encrypted_text, expected_encrypted_text)

    def test_same_characters_key(self):
        """ Repeated characters input key """
        text_to_encrypt = "Si la vida te da limones"
        key = "limonada"

        expected_encrypted_text = "3f004d030f41120808084d1b0b4100004c050402010f0112"

        encrypted_text = CipherEngine.EncryptText(text_to_encrypt, key)

        self.assertEqual(encrypted_text, expected_encrypted_text)
    
    def test_same_characters_text(self):
        """ Repeated characters input text """
        text_to_encrypt = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        key = "repetido"

        expected_encrypted_text = "332431243528252e332431243528252e332431243528252e332431243528252e332431243528252e3324"

        encrypted_text = CipherEngine.EncryptText(text_to_encrypt, key)

        self.assertEqual(encrypted_text, expected_encrypted_text)

    def test_number_text(self):
        """ Number input text """
        text_to_encrypt = "3.14159265359"
        key = "Pi"

        expected_encrypted_text = "6347615d615c695b665c635c69"

        encrypted_text = CipherEngine.EncryptText(text_to_encrypt, key)

        self.assertEqual(encrypted_text, expected_encrypted_text)

    def test_empty_text(self):
        """ empty input text """
        text_to_encrypt = None
        key = "6042380541"

        self.assertRaises( EmptyTextError, CipherEngine.EncryptText, text_to_encrypt, key )

    def test_empty_key(self):
        """ empty input key """
        text_to_encrypt = "Mañana te espero detrás de la fuente"
        key = None

        self.assertRaises( EmptyKeyError, CipherEngine.EncryptText, text_to_encrypt, key )

    def test_special_character_key(self):
        """ special characters input key """
        text_to_encrypt = "Mañana hay examen de cálculo"
        key = "$oñ@r."

        self.assertRaises( KeyCharacterError, CipherEngine.EncryptText, text_to_encrypt, key )

    def test_longer_key(self):
        """ Input key is longer than the input text """
        text_to_encrypt = "P"
        key = "1025789634"

        self.assertRaises( LongerKeyError, CipherEngine.EncryptText, text_to_encrypt, key )


    def test_correct_decryption(self):
        """ Normal input encrypted text and key  """
        encrypted_text = "614044575353"
        key = "12"

        expected_og_text = "Prueba"

        decrypted_text = CipherEngine.DecryptText(encrypted_text, key)

        self.assertEqual(decrypted_text, expected_og_text)

    def test_correct_decryption2(self):
        """ Normal input encrypted text and key  """
        encrypted_text = "7758515e4c18535b5c127d5940474112425d405018415c4c465c565515515c154c5a501842544a59"
        key = "258"

        expected_og_text = "Emily and Harry were sitting in the park"

        decrypted_text = CipherEngine.DecryptText(encrypted_text, key)

        self.assertEqual(decrypted_text, expected_og_text)
    
    def test_correct_decryption3(self):
        """ Normal input encrypted text and key  """
        encrypted_text = "7e5c4b10565b5c42464c51515b435740185e5a145953505d5e15585e12424d5515415f5d1349455c5143571f18435c5a5e125f57104441541246565f15585441135c595651"
        key = "2380541"

        expected_og_text = "Los computadores no hacen lo que uno quiere, sino lo que uno les dice"

        decrypted_text = CipherEngine.DecryptText(encrypted_text, key)

        self.assertEqual(decrypted_text, expected_og_text)

    def test_alphanumeric_key(self):
        """ Alphanumeric input encryption key """
        encrypted_text = "151952401907455302"
        key = "pw12"

        expected_og_text = "encriptar"

        decrypted_text = CipherEngine.DecryptText(encrypted_text, key)

        self.assertEqual(decrypted_text, expected_og_text)

    def test_one_character_key(self):
        """ One character input encryption key """
        encrypted_text = "41505543504245435e"
        key = "1"

        expected_og_text = "padrastro"

        decrypted_text = CipherEngine.DecryptText(encrypted_text, key)

        self.assertEqual(decrypted_text, expected_og_text)
 
    def test_same_cipher_key(self):
        """ Repeated characters input encryption key """
        encrypted_text = "34031603120f0209"
        key = "fffff"

        expected_og_text = "Repetido"

        decrypted_text = CipherEngine.DecryptText(encrypted_text, key)

        self.assertEqual(decrypted_text, expected_og_text)

    def test_empty_encrypted_text(self):
        """ empty input encrypted text """
        encrypted_text = None
        key = "6042380541"

        self.assertRaises( EmptyTextError, CipherEngine.DecryptText, encrypted_text, key )

    def test_empty_encryption_key(self):
        """ empty input encryption key """
        encrypted_text = "0b070a0f1209"
        key = None

        self.assertRaises( EmptyKeyError, CipherEngine.DecryptText, encrypted_text, key )

    def test_special_character_encryption_key(self): 
        """ special characters input encryption key """
        encrypted_text = "0413030809"
        key = "5@lu.dº"

        self.assertRaises( KeyCharacterError, CipherEngine.DecryptText, encrypted_text, key )

    def test_longer_encryption_key(self):
        """ Input encryption key is longer than the input encrypted text """
        encrypted_text = "57545e"
        key = "Dispositivodevision"

        self.assertRaises( LongerKeyError, CipherEngine.DecryptText, encrypted_text, key )


if __name__ == '__main__':
    unittest.main()