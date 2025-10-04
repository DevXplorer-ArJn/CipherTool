# utils/crypto.py
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def generate_key(key_size=24):
    """Generate a random Triple DES key"""
    key = get_random_bytes(key_size)
    return base64.b64encode(key).decode('utf-8')

def encrypt_message(plaintext, key_b64):
    """Encrypt plaintext using Triple DES"""
    try:
        # Decode the key
        key = base64.b64decode(key_b64)
        
        # Validate key size
        if len(key) not in [16, 24]:
            return None, "Invalid key size. Key must be 16 or 24 bytes."
        
        # Convert plaintext to bytes
        plaintext_bytes = plaintext.encode('utf-8')
        
        # Generate IV and create cipher
        iv = get_random_bytes(8)
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        
        # Encrypt with padding
        padded_data = pad(plaintext_bytes, DES3.block_size)
        ciphertext = cipher.encrypt(padded_data)
        
        # Combine IV and ciphertext, encode to base64
        encrypted_message = base64.b64encode(iv + ciphertext).decode('utf-8')
        
        return encrypted_message, None
        
    except Exception as e:
        return None, f"Encryption error: {str(e)}"

def decrypt_message(encrypted_b64, key_b64):
    """Decrypt encrypted message using Triple DES"""
    try:
        # Decode key and encrypted data
        key = base64.b64decode(key_b64)
        encrypted_data = base64.b64decode(encrypted_b64)
        
        # Validate key size
        if len(key) not in [16, 24]:
            return None, "Invalid key size. Key must be 16 or 24 bytes."
        
        # Extract IV and ciphertext
        iv = encrypted_data[:8]
        ciphertext = encrypted_data[8:]
        
        # Create cipher and decrypt
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        decrypted_padded = cipher.decrypt(ciphertext)
        plaintext_bytes = unpad(decrypted_padded, DES3.block_size)
        
        return plaintext_bytes.decode('utf-8'), None
        
    except Exception as e:
        return None, f"Decryption error: {str(e)}"
