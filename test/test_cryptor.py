# import pytest
import unittest
from src.cryptor import AESCrypto

KEY_STR = "accuinsight+ pipeline sk"
KEY_BYTES = KEY = KEY_STR.encode()

# PASSWORD_STR = password = "@d$w0APs"
PASSWORD_STR = password = "P@s$w0rd"
PASSWORD_BYTES = PASSWORD_STR.encode()

ENCRYPTED_PASSWORD = "U2FsdGVkX19Q7+4CMdtJeNJYOhZ6syZ9DtwN4f9y7po="


# @pytest.fixture
# def test_crypto():

#     cipher = AESCrypto()
#     decrypted = cipher.decrypt(ENCRYPTED_PASSWORD)
#     print("decrypted", decrypted)
#     encrypted = cipher.encrypt(PASSWORD_BYTES)
#     print("encrypted", encrypted)
#     print("new_decrypted", cipher.decrypt(encrypted))

#     assert decrypted == PASSWORD_BYTES
#     assert encrypted == ENCRYPTED_PASSWORD


class TestCryptor(unittest.TestCase):

    def test_cryptor(self):
        cipher = AESCrypto()
        decrypted = cipher.decrypt(ENCRYPTED_PASSWORD)
        print("decrypted", decrypted)
        encrypted = cipher.encrypt(PASSWORD_BYTES)
        print("encrypted", encrypted)
        print("new_decrypted", cipher.decrypt(encrypted))

        assert decrypted == PASSWORD_BYTES
        assert encrypted != ENCRYPTED_PASSWORD