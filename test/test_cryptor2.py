# import pytest
import unittest
from src.cryptor import AESCrypto
from src.cryptor2 import ConnectionCryptor


KEY_STR = "accuinsight+ pipeline sk"
KEY_BYTES = KEY = KEY_STR.encode()

# PASSWORD_STR = password = "@d$w0APs"
PASSWORD_STR = password = "P@s$w0rd"
PASSWORD_BYTES = PASSWORD_STR.encode()

ENCRYPTED_PASSWORD = "U2FsdGVkX19Q7+4CMdtJeNJYOhZ6syZ9DtwN4f9y7po="


class TestCryptor(unittest.TestCase):

    def setUp(self) -> None:
        self.ENCRYPTED_PASSWORD = "U2FsdGVkX19Q7+4CMdtJeNJYOhZ6syZ9DtwN4f9y7po="
        self.KEY_STR = "accuinsight+ pipeline sk"
        self.KEY_BYTES = self.KEY_STR.encode()

        self.PASSWORD_STR = "P@s$w0rd"
        self.PASSWORD_BYTES = self.PASSWORD_STR.encode()

    def test_cryptor(self) -> None:

        # 기존 구현체
        cipher = AESCrypto()
        decrypted = cipher.decrypt(self.ENCRYPTED_PASSWORD)
        print("decrypted", decrypted)
        encrypted = cipher.encrypt(self.PASSWORD_BYTES)
        print("encrypted", encrypted)
        print("new_decrypted", cipher.decrypt(encrypted))

        self.assertEqual(decrypted, self.PASSWORD_BYTES)
        self.assertNotEqual(encrypted, self.ENCRYPTED_PASSWORD)


        # 의존성 변경 구현체
        cryptor = ConnectionCryptor(self.KEY_STR)
        cryptor = ConnectionCryptor(self.KEY_BYTES)

        new_decrypted_bytes = cryptor.decrypt(self.ENCRYPTED_PASSWORD)
        new_decrypted_str = cryptor.decrypt(self.ENCRYPTED_PASSWORD, as_str=True)

        self.assertEqual(new_decrypted_str, self.PASSWORD_STR)
        self.assertEqual(new_decrypted_bytes, self.PASSWORD_BYTES)


        new_encrypted_bytes = cryptor.encrypt(self.ENCRYPTED_PASSWORD)
        new_encrypted_str = cryptor.encrypt(self.ENCRYPTED_PASSWORD, as_str=True)

        self.assertNotEqual(new_encrypted_str, self.ENCRYPTED_PASSWORD)
        self.assertNotEqual(new_encrypted_bytes, self.ENCRYPTED_PASSWORD.encode())


        # 구현체 결과 비교 테스트
        self.assertEqual(decrypted, new_decrypted_bytes)