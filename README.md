# Educational Implementation Of RSA-OAEP Following RFC 8017 In Python

This project is an educational implementation of RSA encryption with OAEP (optimal asymmetric encryption padding) padding, fully written in python.
My goal with this project was to better understand how real-world cryptography works, mainly public key encryption. I also explored the vulnerabilities of raw RSA, and understood the importance of a padding scheme such as OAEP.

Rather than using existing cryptography libraries, I instead implemented RSA key generation, encryption, decryption, OAEP encoding/decoding and MGF1 mask function all from scratch. 
Some libraries I used were 'sympy' for a primality test, 'secrets' for random number generation and 'hashlib' for the SHA256 function.

This project is intended purely for experimentation and learning.

RFC 8017: https://www.rfc-editor.org/rfc/rfc8017.html

## What This Project Is Not / Limitations

This project is NOT intended for real world or production cryptographic use.

Although it follows the structure of RSA-OAEP as described in RFC 8017, it does not have protection against multiple types of side-channel attacks such as cache attacks or memory based leaks.
Python does not provide constant-time guarantees for big-integer arithmetic.
This implementation focuses on correct coding structure and learning instead of hard security for real world applications.

## Cryptographic Design

### RSA

RSA is an encryption method that relies on the difficulty of factoring a large number n into its prime components p and q
It uses n = p * q, public exponent 'e' and private exponent 'd' such that:

c = m**e (mod n)
m = c**d (mod n)
'm' is the message and 'c' the ciphertext.

where:
e*d = 1 (mod phi(n)), e and d are modular inverses

and phi(n) is euler's totient function with input n:
phi = (p-1) * (q-1)

I chose 'e' as 2**16 + 1, or 65537, which is a prime number that works very cleanly with RSA and optimizes the program

However, RSA by itself is deterministic and vulnerable to multiple types of attacks. This led me to learning and implementing OAEP

### OAEP

OAEP (Optimal Asymmetric Encryption Padding) is a padding scheme that transforms a message 'm' into a randomized, fixed length encoded message 'EM'. This solves the deterministic problem with RSA and makes it more secure.

OAEP uses:
A cryptographic hash function (SHA256)
A mask function (MGF1)
XOR-based masking and unmasking

OAEP steps:
It builds a fixed-lenght data block with the message inside, DB == (labelhash || padding zeros || 0x01 || message)
Then it uses a random seed and masking to create the EM, EM == (0x00 || masked seed || masked data block)
The EM is encrypted and decrypted through RSA
The message is recovered by unmasking the seed and the data block, followed by extracting the message

The random seed ensures that identical messages encrypt to different ciphertexts.

## File structure

RSA_OAEP/
main.py

RSA/
keygen.py
encrypt.py
decrypt.py

OAEP/
OAEP_encode.py
OAEP_decode.py
mask_function.py

README.md

## How to run

Requirements: 
Python 3.10+
Sympy library
1. Clone the repository
2. Run:
   ```bash
   python main.py

Follow the instructions to:
1. Generate keys
2. Encrypt a message
3. Decrypt a message

## Security Limitations

This program is vulnerable to timing and side channel attacks
The only padding oracle protection is uniform error handling
Prime generation and RSA math rely on python's big integer arithmetic instead of cryptographic libraries
No secure memory handling is performed

These vulnerabilities are intentional as this program is intended for educational purposes, focusing on proper RSA-OAEP structure and understanding

## What I Learned

Through this project I learned that correctly implementing cryptography goes way beyond understanding the mathematics behind it.
Small implementation details, such as byte lenght consistency, padding structure and uniform error handling were critical for security.
I also learned why real world cryptography uses carefully created libraries instead of custom implementations. 
Overall, this project deepened my interest in cryptography and cyber-security.
This project was also a great way to strengthen my python skills.



