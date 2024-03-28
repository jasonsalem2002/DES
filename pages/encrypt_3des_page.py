import tkinter as tk
from tkinter import *
from functions.utils import validate_hex
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
            rkb = keyGeneration(key)
            rk = [format(int(keyR, 2), '012X') for keyR in rkb]
            ciphertext = triple_des_encrypt(plaintext, keyb, triple_des_keys)
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