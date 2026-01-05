import hashlib

def MGF1(seed, ml): #necessary for OAEP encoding. Is irreversible due to built-in hash function. Extends the seed to desired lenght while hashing. Deterministic
    hl = hashlib.sha256().digest_size #Sha 256 is the only hash used in this program, hash lenght is 32 bytes uniformily
    t = b''
    c = 0

    while len(t) < ml:
        cb = int.to_bytes(c, 4,'big')
        t += hashlib.sha256(seed+cb).digest()
        c += 1

    return t[:ml]
