import sys

from RSA.keygen import generate
from RSA.encrypt import encrypt_input
from RSA.decrypt import decrypt_input


def main():
    print("This is an educational RSA-OAEP cryptography system. THIS IS NOT SECURE AND ONLY AN EXPERIMENTAL MODEL OF RSA ENCRYPTION! ONLY USE IT TO LEARN!")
    try:
        while True:
            decision = int(input("Type '1' if you wish to generate a private and public key. Type '2' is you wish to encrypt a message. Type '3' is you wish to decrypt a message. Type '4' is you wish to exit. "))
            if decision == 1:
                generate()
                break
            elif decision == 2:
                encrypt_input()
                break
            elif decision == 3:
                decrypt_input()
                break
            elif decision == 4:
                sys.exit()
            else:
                print("Please only input 1,2,3 or 4")
    except ValueError:
        sys.exit("An error occured. ") #To prevent giving attackers information, all errors must be handled uniformly. Any checks for validitly raise a ValueError that comes back to this line.
    

main()