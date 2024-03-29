import tkinter as tk
from tkinter import *
from functions.utils import validate_hex, keyGeneration
from encryptionFunctions.Triple_DES_encryption import triple_des_encrypt

def encrypt_triple_des():

    root = tk.Tk()
    root.title("Encrypt Triple DES")
    root.geometry("800x600")

    # add button that triggers key generation later

    global output

    def handle_encryption(event=None):
        plaintext=plaintext_entry.get()
        key=key_entry.get()
        if (plaintext and key):

            plaintext = "123456ABCD132536"

            key1 = "AABB09182736CCDD"
            key2 = "1122334455667788" 
            key3 = "BBCCDDEEFF001122"  

            '''
            do not change the next lines, you have to use the keys above, find a way to 
            pass them from the UI to the function. 
            '''

            rkb1 = keyGeneration(key1)
            rkb2 = keyGeneration(key2)
            rkb3 = keyGeneration(key3)

            rk1 = [format(int(keyR, 2), '012X') for keyR in rkb1]
            rk2 = [format(int(keyR, 2), '012X') for keyR in rkb2]
            rk3 = [format(int(keyR, 2), '012X') for keyR in rkb3]
            triple_des_keys = [rk1, rk2, rk3]
            keyb = [rkb1, rkb2, rkb3]

            ciphertext = triple_des_encrypt(plaintext,keyb, triple_des_keys)
            print("Triple DES Encrypted Cipher Text:", ciphertext)
            output.config(state="normal")
            output.delete('1.0', tk.END)
            output.insert(tk.END, ciphertext)
            output.config(state="disabled")

    plaintext_label = tk.Label(root, text="plaintext")
    plaintext_label.grid(row=0, column=0, padx=10, pady=10)
    isHex = (root.register(validate_hex), '%P')
    plaintext_entry = tk.Entry(root, validate="key", validatecommand=isHex)
    plaintext_entry.grid(row=0, column=1, padx=10, pady=10)

    key_label = tk.Label(root, text="Key:")
    key_label.grid(row=1, column=0, padx=10, pady=10)
    key_entry = tk.Entry(root, validate='key', validatecommand=isHex)
    key_entry.grid(row=1, column=1, padx=10, pady=10)

    trigger = tk.Button(root, text="Encrypt", command=handle_encryption)
    trigger.grid(row=0, column=4, padx=10, pady=10)
    plaintext_entry.bind("<Return>", lambda event: handle_encryption())

    output = tk.Text(root, height=32, width=40, state=DISABLED)  
    output.grid(row=3, column=0)


    root.mainloop