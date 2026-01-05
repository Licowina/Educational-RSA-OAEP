import hashlib
import sys

from OAEP.mask_function import MGF1

def oaep_decode(m,n): #OAEP's uniform structure allows us to decode the EM step-by-step
    db = extract_db(m,n)
    mb = extract_m(db,n)
    msg = translate(mb)
    return msg

#All ValueErrors that are raised are checks for the messages integrity. This prevents corrupted and altered messages to make it through as their structure changes
def extract_db(m,n):
    k = (n.bit_length()+7)//8 #Consistent K value must also be maintained in decoding
    hlen = hashlib.sha256().digest_size
    EM = int.to_bytes(m,k,'big') #RSA only works with integers, so integers to bytes conversion must be made before decoding. Must ensure byte lenght K so leading zeros are not lost
    if EM[0] != 0: 
        raise ValueError
    if len(EM) != k:
        raise ValueError
    mseed = EM[1:hlen+1]
    mdb = EM[hlen+1:] 
    #Unmasking of the seed and db uses the XOR property "A XOR B XOR B = A". Makes it possible to extract the real data
    seedmask = MGF1(mdb, len(mseed))
    seed = bytes(a^b for a,b in zip(mseed, seedmask))
    dbmask = MGF1(seed, len(mdb))
    return bytes(a^b for a,b in zip(mdb, dbmask))

def extract_m(db,n):
    lh = hashlib.sha256(b'').digest()
    if db[0:32] != lh:
        raise ValueError 
    check = 0
    for i in range(len(lh), len(db)): #Message is always placed after padding zeros and a 0x01 header. This makes scanning for it possible
        if db[i] == 0:
            continue
        if db[i] == 1:
            check = 1
            break
        else:
            raise ValueError
    if check != 1:
        raise ValueError
    return db[i+1:]

def translate(msg):
    try:
        return msg.decode('utf-8')
    except UnicodeDecodeError:
        raise ValueError