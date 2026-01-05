import sys

from OAEP.OAEP_decode import oaep_decode

def decrypt_input():
    print("We will now decrypt your message")
    n = int(input("Type your public 'n' value. "))
    d = int(input("Type you private 'd' value. "))
    c = int(input("Type the message you wish to decrypt. "))
    if c >= n:
        raise ValueError
    if c < 0: #Negative ciphertextxs must be checked and rejected as well
        raise ValueError 
    m = decrypt_rsa(c,d,n)
    msg = oaep_decode(m,n)
    print(f"This is the decrypted message\n\n{msg}")

def decrypt_rsa(c,d,n):
    return pow(c,d,n) #RSA funtion