import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from encryptionFunctions.DES_encryption import encrypt
from decryptionFunctions.DES_decryption import decrypt

def triple_des_encrypt(message,keyBinary, keys):
    output, ciphertext = encrypt(message, keyBinary[0], keys[0])
    #print("First DES Encrypted Cipher Text:", output)
    outputDec, ciphertextDec = decrypt(ciphertext, keyBinary[1])
    #print("First DES Decrypted Cipher Text:", outputDec)
    final, ciphertextEnc = encrypt(ciphertextDec, keyBinary[2], keys[2])
    #print("Second DES Encrypted Cipher Text:", final)
    #return ciphertextEnc
    return final