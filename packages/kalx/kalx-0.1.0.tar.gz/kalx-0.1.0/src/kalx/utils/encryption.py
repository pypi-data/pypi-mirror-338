"""
Encryption utilities for sensitive data.
"""
import os
import base64
from cryptography.fernet import Fernet
from pathlib import Path

def get_or_create_key():
    """Get encryption key from env or generate one."""
    key = os.environ.get('KALX_ENCRYPTION_KEY')
    if not key:
        key = Fernet.generate_key()
        # Print key for developer to save
        print(f"Generated new encryption key: {key.decode()}")
        print("Set this as KALX_ENCRYPTION_KEY environment variable")
    else:
        key = key.encode()
    return key

def encrypt_credentials(data: str) -> str:
    """Encrypt credentials using Fernet."""
    f = Fernet(get_or_create_key())
    return base64.b64encode(f.encrypt(data.encode())).decode()

def decrypt_credentials(encrypted_data: str) -> str:
    """Decrypt credentials using Fernet."""
    try:
        f = Fernet(get_or_create_key())
        return f.decrypt(base64.b64decode(encrypted_data.encode())).decode()
    except Exception as e:
        raise ValueError("Failed to decrypt credentials. Check KALX_ENCRYPTION_KEY environment variable.")
