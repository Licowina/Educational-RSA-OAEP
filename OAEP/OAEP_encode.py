import hashlib
import secrets
import sys

from OAEP.mask_function import MGF1

def oaep_encode(msg, n):
    k = (n.bit_length()+7)//8 #Consistent K value must be maintained in all of OAEP. Ensures proper structure. This line of code can be seen in all OAEP functions
    hlen = hashlib.sha256().digest_size #Lenght of hash function, 32 bytes for SHA256, must also be consistently used in all OAEP functions
    db = build_db(msg,n)
    EM = build_em(db, n, hlen)
    m = int.from_bytes(EM, 'big') #Consistently use Big endian for all bytes. RSA only works with integers, so bytes to integer conversion must be done before encryption
    return m

def build_db(msg, n):
    k = (n.bit_length()+7)//8
    label = b''
    lh = hashlib.sha256(label).digest()
    mb = msg.encode('utf-8')
    if len(mb) > k - 2 * len(lh) - 2:
        raise ValueError
    N = k - 2 * len(lh) - 2 - len(mb)
    if N < 0:
        raise ValueError
    PS = bytes(N) #Amount of padding zeros is adjusted based on the size of the message to maintain proper data block length
    return lh + PS + b'\x01' + mb #Data block must maintain proper structure. Alway k- hash length -1 bytes long, 233 in this case

#MGF1 and XOR are at the core of OAEP. Main functions in building the encoded message (EM)
#The XOR property "A XOR B XOR B = A" ensures decoding the EM is possible
def build_em(db, n, lenh): 
    k = (n.bit_length()+7)//8
    seed = secrets.token_bytes(lenh)
    dbmask = MGF1(seed,len(db)) 
    mdb = bytes(a^b for a,b in zip(db,dbmask))
    seedmask = MGF1(mdb, len(seed))
    mseed = bytes(a^b for a,b in zip(seed, seedmask))
    if len(b'\x00' + mseed + mdb) != k:
        raise ValueError
    return b'\x00' + mseed + mdb #EM must maintain consistent structure of lenght k: 0x00 + Hash Lenght + Data block lenght