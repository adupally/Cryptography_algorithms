<<<<<<< HEAD
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def encrypt_aes_cbc(key, iv, plaintext):

    # Ensure the plaintext is padded to match block size so that cipher text will be generated for all the input 
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv)) # using the cipher function and inside the function using the aes algorithms passing key parameter and using CBC mode by passing IV 
    encryptor = cipher.encryptor() #encryptor function encrypts the cipher(above variable cipher)
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize() #here it finally encrypt the padded_plaintext and store the ciphertext in ciphertext varaiable

    return ciphertext

def decrypt_aes_cbc(key, iv, ciphertext):

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
   
    # Remove padding to get the original plaintext
    # if we don;t use padding then the ouput plaintext will be in multiple of 8 only it does not encrypt the other plaintext remaining of text (reamining of block size) 
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext
# To use os.urandom() need to immport os
# Example usage:
key = b'qwseryhsvadwesdy' # we give key harcode or we can also use random key using function  os.urandom(keysize) 
iv = os.urandom(128//8) # for IV  we need to use os.urandom(ivsize) because it generate the differenr cipher text for same plaintext also
plaintext = b'Hello, this is a secret message! thirumal reddy'

ciphertext = encrypt_aes_cbc(key, iv, plaintext)
print("Ciphertext:", ciphertext)

decrypted_data = decrypt_aes_cbc(key, iv, ciphertext)
print("Decrypted data:", decrypted_data.decode('utf-8'))
=======
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def encrypt_aes_cbc(key, iv, plaintext):

    # Ensure the plaintext is padded to match block size so that cipher text will be generated for all the input 
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv)) # using the cipher function and inside the function using the aes algorithms passing key parameter and using CBC mode by passing IV 
    encryptor = cipher.encryptor() #encryptor function encrypts the cipher(above variable cipher)
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize() #here it finally encrypt the padded_plaintext and store the ciphertext in ciphertext varaiable

    return ciphertext

def decrypt_aes_cbc(key, iv, ciphertext):

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
   
    # Remove padding to get the original plaintext
    # if we don;t use padding then the ouput plaintext will be in multiple of 8 only it does not encrypt the other plaintext remaining of text (reamining of block size) 
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext
# To use os.urandom() need to immport os
# Example usage:
key = b'qwseryhsvadwesdy' # we give key harcode or we can also use random key using function  os.urandom(keysize) 
iv = os.urandom(128//8) # for IV  we need to use os.urandom(ivsize) because it generate the differenr cipher text for same plaintext also
plaintext = b'Hello, this is a secret message! thirumal reddy'

ciphertext = encrypt_aes_cbc(key, iv, plaintext)
print("Ciphertext:", ciphertext)

decrypted_data = decrypt_aes_cbc(key, iv, ciphertext)
print("Decrypted data:", decrypted_data.decode('utf-8'))
>>>>>>> 89d316d659367f7708f9d6c79b86ab6c2f47e1bf
