import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from decryptionFunctions.DES_decryption import decrypt
from encryptionFunctions.DES_encryption import encrypt

def triple_des_decrypt(ciphertext, keyBinary, keys):
    outputDec, intermediate_text = decrypt(ciphertext, keyBinary[2])
    #print("Second DES Decrypted Intermediate Text:", outputDec)
    output, intermediate_text_dec = encrypt(intermediate_text, keyBinary[1], keys[1])
    #print("First DES Decrypted Intermediate Text:", output)
    plaintext, _ = decrypt(intermediate_text_dec, keyBinary[0])
    #print("First DES Decrypted Plain Text:", plaintext)
    everything = outputDec + "\n" + output + "\n" + plaintext
    return everything


