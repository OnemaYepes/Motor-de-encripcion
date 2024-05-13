import unittest

import sys
sys.path.append("src")

from model.CipherEngine import CipherEngine
from model.CipherError import EmptyTextError, EmptyKeyError, KeyCharacterError, LongerKeyError

class CipherTest( unittest.TestCase ):
    def test_longer_encryption_key(self):
        """ Input encryption key is longer than the input encrypted text """
        encrypted_text = "57545e"
        key = "Dispositivodevision"

        self.assertRaises( LongerKeyError, CipherEngine.DecryptText, encrypted_text, key )


if __name__ == '__main__':
    unittest.main()