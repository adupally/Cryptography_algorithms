# Cryptography_algorithms
Introduction
============

This repository is dedicated to the implementation and exploration of various symmetric and asymmetric cryptography algorithms. Cryptography is an essential aspect of modern information security, enabling secure communication, data protection, and authentication.

Table of Contents
==================

Symmetric Cryptography
======================

1 Advanced Encryption Standard

2 Triple Data Encryption Standard

Asymmetric Cryptography
=======================

1 Rivest-Shamir-Adleman

2 Elliptic Curves

Symmetric Cryptography
======================

Symmetric cryptography involves the use of a single secret key for both encryption and decryption.This section will contain implementations of some popular symmetric cryptographic algorithms.

Advanced Encryption Algorithm (AES)
===================================

The AES algorithm operates on fixed-size blocks of data, and the key size determines the security level and the number of encryption rounds used during the encryption process.

In AES, each round of encryption consists of four main operations:

      SubBytes: Substitutes each byte of the state with a corresponding byte from a fixed substitution table (S-box).

      ShiftRows: Shifts the rows of the state matrix by varying offsets.

      MixColumns: Mixes the columns of the state matrix using a mathematical transformation.(except for the last round).

      AddRoundKey: Performs a bitwise XOR between the state matrix and the round key. 

For AES-128 the encryption process consists of 10 rounds, while AES-192 and AES-256 use 12 and 14 rounds, respectively.

We need use IV (Initialization Vector) is a crucial component used in certain modes of operation to add randomness and improve security. 

     We use IV in CBC mode of operation only 
  
     We don't use in EBC mode of operation because it encrypts each block of plaintext independently 
 
As i am using cryptography library for different modes of operations

"pip install cryptography" command to install cryptography 

"from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes" using this you will import all the algorithms and modes of operations

There are different types of modes of operations
     like CBC,ECB,CTB,CTR,CFB Etc
     In this we mainly focusing on  CBC, ECB modes of operations

we need to use padding for make the block size complete 

In ECB mode of operation we get the same cipher text every time we use same key and same plaintext so it's not used more

In CBC mode of operation we get different cipher text every time even though we use samke key and plain text because we change the IV value every time.So it is used in wide range of applications

Triple Data Encryption Standard (3DES)
======================================

In Triple DES (3DES), each of the three keys is applied for 16 rounds of encryption in the process. This results in a total of 48 rounds of encryption when using three different keys.  

Key size = 56bits 

for implementing TDES we have three types for key represenattion

     1 : Need have three different Keys 

     2: Can have 2 different keys k1,k2,k1

     3: Can use same three keys (not recommended)

 Formula  ciphertext = E(K3, D(K2, E(K1, plaintext)))

In TripleDES also we use modes of operation and modes of operations work asame as AES

In TDES we use pycryptodome library 

command to install libaray "pip install pycryptodome"




