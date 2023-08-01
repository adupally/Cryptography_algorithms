from Cryptodome.Cipher import DES3
from Cryptodome.Random import get_random_bytes

def pad(text, block_size):
    pad_len = block_size - len(text) % block_size
    return text + bytes([pad_len] * pad_len)

def unpad(padded_text):
    return padded_text[:-padded_text[-1]]

def encrypt_3des_ecb(key1, key2, key3, plaintext):
    cipher = DES3.new(key1, DES3.MODE_ECB)
    intermediate = cipher.encrypt(pad(plaintext, DES3.block_size))

    cipher = DES3.new(key2, DES3.MODE_ECB)
    intermediate = cipher.decrypt(intermediate)

    cipher = DES3.new(key3, DES3.MODE_ECB)
    ciphertext = cipher.encrypt(intermediate)

    return ciphertext

def decrypt_3des_ecb(key1, key2, key3, ciphertext):
    cipher = DES3.new(key3, DES3.MODE_ECB)
    intermediate = cipher.decrypt(ciphertext)

    cipher = DES3.new(key2, DES3.MODE_ECB)
    intermediate = cipher.encrypt(intermediate)

    cipher = DES3.new(key1, DES3.MODE_ECB)
    plaintext = unpad(cipher.decrypt((intermediate)))

    return plaintext

# Example usage:
key1 = get_random_bytes(24)  # 24 bytes (64 bits) for the first 3DES key or we can use os.urandom(24)
key2 = get_random_bytes(24)  # 24 bytes (64 bits) for the second 3DES key or we can use os.urandom(24)
key3 = get_random_bytes(24)  # 24  bytes (64 bits) for the third 3DES key or we can use os.urandom(24)
plaintext = b'Hello, this is a secret message! thirumal ereddyt'

ciphertext = encrypt_3des_ecb(key1, key2, key3, plaintext)
print("Ciphertext:", ciphertext.hex())

decrypted_data = decrypt_3des_ecb(key1, key2, key3, ciphertext)
print("Decrypted data:", decrypted_data.decode('utf-8'))
