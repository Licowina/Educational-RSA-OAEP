import sys

from OAEP.OAEP_encode import oaep_encode

def encrypt_input():
    print("We will now encrypt your message")
    n = int(input("Type the receiver's public 'n' value. "))
    e = int(input("Type the receiver's public 'e' value. "))
    msg = str(input("Type the message you wish to send. "))
    m = oaep_encode(msg, n)
    c = encrypt_rsa(m,e,n)
    print(f"This is your encrypted message\n\n{c}\n\nsend this to the receiver!")

def encrypt_rsa(m,e,n):
    return pow(m,e,n) #RSA function