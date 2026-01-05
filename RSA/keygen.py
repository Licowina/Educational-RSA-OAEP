from secrets import randbits
from math import gcd
import sys

from sympy import isprime
#RSA stems from 2 distinct primes, p and q, which are multiplied to generate n. Factoring n is considered mathematically hard.
def prime_gen():
    while True:
        prime = randbits(1024) | 1 | (1 << 1023) #2 1024-bit primes, when multiplied create a 2048-bit number (n) which is used for the modulus, thus 2048-bit RSA
        if isprime(prime):
            return prime

def generate():
    while True:
        p = prime_gen()
        q = prime_gen()
        if p != q:
            break
    n = p * q 
    e = 2**16 + 1 #public exponent
    phi = (p-1)*(q-1) #Euler's totient only used to compute d
    if gcd(e,phi) != 1:
        sys.exit("Key generation failed, please try again. ")
    d = pow(e, -1, phi) #private exponent
    print(f"Your public key is the following:\n\nn=\n{n}\n\ne=\n{e}\n\nFeel free to publish them!")
    print(f"Your private key is the following:\n\nd=\n{d}\n\nKeep this a secret!")