import tkinter as tk
from tkinter import messagebox
from tkinter import *
from functions.utils import validate_hex
from decryptionFunctions.DES_decryption import decrypt

def decrypt_des_test():
    root = tk.Tk()
    root.title("Decrypt DES")
    root.geometry("400x500")

    isHex = (root.register(validate_hex), '%P')

    ciphertext_label = tk.Label(root, text="Ciphertext:")
    ciphertext_label.grid(row=0, column=0, padx=10, pady=10)
    ciphertext_entry = tk.Entry(root, validate="key", validatecommand=isHex)
    ciphertext_entry.grid(row=0, column=1, padx=10, pady=10)

    key_label = tk.Label(root, text="Key:")
    key_label.grid(row=1, column=0, padx=10, pady=10)
    key_entry = tk.Entry(root, validate='key', validatecommand=isHex)
    key_entry.grid(row=1, column=1, padx=10, pady=10)

    ciphertext = ciphertext_entry.get()
    key = key_entry.get()

    output = decrypt(ciphertext, key)
    #output.grid(row=4, column=0)


