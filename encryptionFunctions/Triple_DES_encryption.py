import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

# the above was written by chat gpt to fix import errors

from functions.utils import keyGeneration
from encryptionFunctions.DES_encryption import encrypt
from decryptionFunctions.DES_decryption import decrypt

def triple_des_encrypt(message,keyBinary, keys):
    output, ciphertext = encrypt(message, keyBinary[0], keys[0])
    print("First DES Encrypted Cipher Text:", output)
    outputDec, ciphertextDec = decrypt(ciphertext, keyBinary[1])
    print("First DES Decrypted Cipher Text:", outputDec)
    final, ciphertextEnc = encrypt(ciphertextDec, keyBinary[2], keys[2])
    print("Second DES Encrypted Cipher Text:", final)
    return ciphertextEnc

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
ciphertext = triple_des_encrypt(plaintext,keyb, triple_des_keys)
print("Triple DES Encrypted Cipher Text:", ciphertext)
