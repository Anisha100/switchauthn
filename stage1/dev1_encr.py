
Pythonfrom Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import sys

def generate_keys(key_size=2048):

    try:
        key = RSA.generate(key_size)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return private_key, public_key
    except Exception as e:
        print(f"Error generating keys: {e}")
        sys.exit(1)

def encrypt_message(message, public_key_data):
   
    try:
        public_key = RSA.import_key(public_key_data)
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher.encrypt(message.encode('utf-8'))
        return encrypted_data
    except Exception as e:
        print(f"Encryption error: {e}")
        sys.exit(1)

def decrypt_message(encrypted_data, private_key_data):
    
    try:
        private_key = RSA.import_key(private_key_data)
        cipher = PKCS1_OAEP.new(private_key)
        decrypted_data = cipher.decrypt(encrypted_data)
        return decrypted_data.decode('utf-8')
    except Exception as e:
        print(f"Decryption error: {e}")
        sys.exit(1)

if __name__ == "__main__":
  
    private_key, public_key = generate_keys()

    print("=== RSA Keys Generated ===")
    print("Private Key:\n", private_key.decode())
    print("Public Key:\n", public_key.decode())

   
    message = "Hello, RSA encryption in Python!"
    encrypted = encrypt_message(message, public_key)
    print("\nEncrypted Message (bytes):", encrypted)

 
    decrypted = decrypt_message(encrypted, private_key)
    print("\nDecrypted Message:", decrypted)



