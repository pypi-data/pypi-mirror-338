import unittest

import os
import json
import base64

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from demexpy.encryption import (
    generate_x25519_keypair, 
    private_key_to_string, 
    public_key_to_string,
    private_key_from_string, 
    public_key_from_string, 
    derive_shared_secret,
    derive_symmetric_key, 
    encrypt_aes_gcm, 
    decrypt_aes_gcm, 
    decrypt_str,
    encrypt_str
)

class TestEncryption(unittest.TestCase):
    def test_private_key_from_string(self):
        private_key, _ = generate_x25519_keypair()
        private_key_string = private_key_to_string(private_key)
        gen_private_key =private_key_from_string(private_key_string)

        assert isinstance(gen_private_key, x25519.X25519PrivateKey)
        
        self.assertEqual(
            private_key.private_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PrivateFormat.Raw,
                encryption_algorithm=serialization.NoEncryption(),
            ),
            gen_private_key.private_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PrivateFormat.Raw,
                encryption_algorithm=serialization.NoEncryption(),
            ),
        )

    def test_public_key_from_string(self):
        _, public_key = generate_x25519_keypair()
        public_key_string = public_key_to_string(public_key)
        gen_public_key = public_key_from_string(public_key_string)

        assert isinstance(gen_public_key, x25519.X25519PublicKey)

        self.assertEqual(
            public_key.public_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PublicFormat.Raw,
            ),
            gen_public_key.public_bytes(
                encoding=serialization.Encoding.Raw,
                format=serialization.PublicFormat.Raw,
            ),
        )

    def test_key_derivation(self):
        aliceprivate_key, alicepublic_key = generate_x25519_keypair()
        bobprivate_key, bobpublic_key = generate_x25519_keypair()
        secret_message = json.dumps(
            {
                "message": "Hello, world!"
            }
        )

        # test shared secret derivation
        alice_shared_secret = derive_shared_secret(aliceprivate_key, bobpublic_key)
        bob_shared_secret = derive_shared_secret(bobprivate_key, alicepublic_key)

        self.assertEqual(
            alice_shared_secret,
            bob_shared_secret
        )

        # test symmetric key derivation
        alice_symmetric_key = derive_symmetric_key(alice_shared_secret)
        bob_symmetric_key = derive_symmetric_key(bob_shared_secret)

        self.assertEqual(
            alice_symmetric_key,
            bob_symmetric_key
        )

    def test_encryption_decryption(self):
        aliceprivate_key, alicepublic_key = generate_x25519_keypair()
        bobprivate_key, bobpublic_key = generate_x25519_keypair()
        secret_message = json.dumps(
            {
                "message": "Hello, world!"
            }
        )

        # test encryption decryption
        alice_encrypted_message = encrypt_str(
            secret_message.encode("utf-8"),
            private_key_to_string(aliceprivate_key),
            public_key_to_string(bobpublic_key)
        )

        bob_decrypted_message = decrypt_str(
            alice_encrypted_message["nonce"], 
            alice_encrypted_message["ciphertext"], 
            alice_encrypted_message["tag"], 
            private_key_to_string(bobprivate_key), 
            public_key_to_string(alicepublic_key)
        )

        self.assertEqual(
            bob_decrypted_message,
            secret_message
        )





if __name__ == '__main__':
    unittest.main()
