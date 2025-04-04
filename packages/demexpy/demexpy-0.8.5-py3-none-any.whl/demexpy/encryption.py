import os
import json
import base64

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


# KEYGEN
def generate_x25519_keypair():
    private_key = x25519.X25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key

def private_key_to_string(private_key):
    private_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    )

    return base64.b64encode(private_bytes).decode('utf-8')

def public_key_to_string(public_key):
    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )

    return base64.b64encode(public_bytes).decode('utf-8')

def private_key_from_string(private_key_string):
    try:
        private_bytes = base64.b64decode(private_key_string)
    except Exception:
        raise ValueError("Invalid base64 private key encoding")

    if len(private_bytes) != 32:
        raise ValueError("Invalid private key length")
    return x25519.X25519PrivateKey.from_private_bytes(private_bytes)

def public_key_from_string(public_key_string):
    try:
        public_bytes = base64.b64decode(public_key_string)
    except Exception:
        raise ValueError("Invalid base64 public key encoding")

    if len(public_bytes) != 32:
        raise ValueError("Invalid public key length")
    return x25519.X25519PublicKey.from_public_bytes(public_bytes)





# KEY DERIVATION
def derive_shared_secret(private_key, peer_public_key):
    if not isinstance(private_key, x25519.X25519PrivateKey):
        raise ValueError("Invalid private key type")

    if not isinstance(peer_public_key, x25519.X25519PublicKey):
        raise ValueError("Invalid public key type")

    try:
        return private_key.exchange(peer_public_key)
    except Exception as e:
        raise ValueError(f"Failed to derive shared secret: {str(e)}")


def derive_symmetric_key(shared_secret):
    if len(shared_secret) != 32:
        raise ValueError("Invalid shared secret length")
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256 key
        salt=None,
        info=b"key-exchange",
    )
    return hkdf.derive(shared_secret)





# ENCRYPTION/DECRYPTION
def encrypt_aes_gcm(key, plaintext):
    if len(key) != 32:
        raise ValueError("Invalid AES key length: must be 32 bytes")

    nonce = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return {
        "nonce": base64.b64encode(nonce).decode(),
        "ciphertext": base64.b64encode(ciphertext).decode(),
        "tag": base64.b64encode(encryptor.tag).decode()
    }

def decrypt_aes_gcm(key, nonce, ciphertext, tag):
    if len(key) != 32:
        raise ValueError("Invalid AES key length: must be 32 bytes")

    nonce = base64.b64decode(nonce)
    ciphertext = base64.b64decode(ciphertext)
    tag = base64.b64decode(tag)

    if len(nonce) != 12:
        raise ValueError("Invalid nonce length: must be 12 bytes")
    if len(tag) != 16:
        raise ValueError("Invalid tag length: must be 16 bytes")

    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag))
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()







# HIGHER LEVEL FUNCTIONS
def encrypt_str(obj_str_bytes, private_key_str, public_key_str):
    if not isinstance(obj_str_bytes, bytes):
        raise ValueError("Input object must be passed as bytes")
    
    try:
        obj_str_bytes.decode("utf-8")  # Ensure it's UTF-8 encoded
        json.loads(obj_str_bytes)  # Validate JSON format
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise ValueError("Invalid JSON string provided")

    private_key = private_key_from_string(private_key_str)
    public_key = public_key_from_string(public_key_str)

    shared_secret = derive_shared_secret(private_key, public_key)
    symmetric_key = derive_symmetric_key(shared_secret)

    return encrypt_aes_gcm(symmetric_key, obj_str_bytes)


def decrypt_str(nonce, ciphertext, tag, private_key_str, public_key_str):
    try:
        private_key = private_key_from_string(private_key_str)
        public_key = public_key_from_string(public_key_str)
        shared_secret = derive_shared_secret(private_key, public_key)
        symmetric_key = derive_symmetric_key(shared_secret)
        decrypted_message = decrypt_aes_gcm(symmetric_key, nonce, ciphertext, tag).decode('utf-8')
        return decrypted_message
    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")
