<<<<<<< HEAD
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def pad(text, block_size):
    # We use PKCS#7 padding
    padding_size = block_size - (len(text) % block_size)
    return text + bytes([padding_size]) * padding_size

def unpad(padded_text):
    padding_size = padded_text[-1]
    return padded_text[:-padding_size]

def encrypt_aes_ecb(key, plaintext):

    # Ensure the plaintext is padded to match block size
    block_size = algorithms.AES.block_size // 8
    padded_plaintext = pad(plaintext, block_size)

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    return ciphertext

def decrypt_aes_ecb(key, ciphertext):

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding to get the original plaintext
    plaintext = unpad(padded_plaintext)

    return plaintext

# Example usage:
key = b'ThisIsASecretKey'
plaintext = b'Hello, this is a secret message!'

ciphertext = encrypt_aes_ecb(key, plaintext)
print("Ciphertext:", ciphertext)

decrypted_data = decrypt_aes_ecb(key, ciphertext)
print("Decrypted data:", decrypted_data.decode('utf-8'))
=======
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def pad(text, block_size):
    # We use PKCS#7 padding
    padding_size = block_size - (len(text) % block_size)
    return text + bytes([padding_size]) * padding_size

def unpad(padded_text):
    padding_size = padded_text[-1]
    return padded_text[:-padding_size]

def encrypt_aes_ecb(key, plaintext):

    # Ensure the plaintext is padded to match block size
    block_size = algorithms.AES.block_size // 8
    padded_plaintext = pad(plaintext, block_size)

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    return ciphertext

def decrypt_aes_ecb(key, ciphertext):

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding to get the original plaintext
    plaintext = unpad(padded_plaintext)

    return plaintext

# Example usage:
key = b'ThisIsASecretKey'
plaintext = b'Hello, this is a secret message!'

ciphertext = encrypt_aes_ecb(key, plaintext)
print("Ciphertext:", ciphertext)

decrypted_data = decrypt_aes_ecb(key, ciphertext)
print("Decrypted data:", decrypted_data.decode('utf-8'))
>>>>>>> 89d316d659367f7708f9d6c79b86ab6c2f47e1bf
