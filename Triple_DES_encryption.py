from functions.utils import keyGeneration
from DES_encryption import encrypt
from DES_decryption import decrypt

def triple_des_encrypt(message, keys):
    ciphertext = encrypt(message, keyb[0], keys[0])
    print("First DES Encrypted Cipher Text:", ciphertext)
    ciphertextDec = decrypt(ciphertext, keyb[1])
    print("First DES Decrypted Cipher Text:", ciphertextDec)
    ciphertextEnc = encrypt(ciphertextDec, keyb[2], keys[2])
    print("Second DES Encrypted Cipher Text:", ciphertextEnc)
    return ciphertext

# Generate three keys for Triple DES
key1 = "AABB09182736CCDD"
key2 = "1122334455667788" 
key3 = "BBCCDDEEFF001122"  

rkb1 = keyGeneration(key1)
rkb2 = keyGeneration(key2)
rkb3 = keyGeneration(key3)

# Convert round keys to hexadecimal strings
rk1 = [format(int(keyR, 2), '012X') for keyR in rkb1]
rk2 = [format(int(keyR, 2), '012X') for keyR in rkb2]
rk3 = [format(int(keyR, 2), '012X') for keyR in rkb3]

# Concatenate round keys for Triple DES
triple_des_keys = [rk1, rk2, rk3]
keyb = [rkb1, rkb2, rkb3]

# Encrypt using Triple DES
plaintext = "123456ABCD132536"
ciphertext = triple_des_encrypt(plaintext, triple_des_keys)
print("Triple DES Encrypted Cipher Text:", ciphertext)
