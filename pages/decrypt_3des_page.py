import tkinter as tk
from tkinter import *
from tkinter import messagebox
from functions.utils import validate_hex, keyGeneration
from decryptionFunctions.Triple_DES_decryption import triple_des_decrypt

def decrypt_triple_des():

    root = tk.Tk()
    root.title("Decrypt Triple DES")
    root.geometry("800x600")

    global output

    def handle_encryption(event=None):
        ciphertext=ciphertext_entry.get()
        key1 = key1_entry.get()
        key2 = key2_entry.get()
        key3 = key3_entry.get()

        if len(ciphertext) != 16:
            messagebox.showerror("Error", "ciphertext must be exactly 16 characters long.")
            return
        if len(key1) != 16 and len(key2) != 16 and len(key3) != 16:
            messagebox.showerror("Error", "Key must be exactly 16 characters long.")
            return

        rkb1 = keyGeneration(key1)
        rkb2 = keyGeneration(key2)
        rkb3 = keyGeneration(key3)

        rk1 = [format(int(keyR, 2), '012X') for keyR in rkb1]
        rk2 = [format(int(keyR, 2), '012X') for keyR in rkb2]
        rk3 = [format(int(keyR, 2), '012X') for keyR in rkb3]
        triple_des_keys = [rk1, rk2, rk3]
        keyb = [rkb1, rkb2, rkb3]

        ciphertext = triple_des_decrypt(ciphertext, keyb, triple_des_keys)
        #print("Triple DES Decrypted Plain Text:", ciphertext)

        output.config(state="normal")
        output.delete('1.0', tk.END)
        output.insert(tk.END, ciphertext)
        output.config(state="disabled")

    frame = tk.Frame(root)
    frame.grid(row=0, column=0, rowspan=4, columnspan=3)

    ciphertext_label = tk.Label(frame, text="ciphertext")
    ciphertext_label.grid(row=0, column=0, padx=10, pady=10)
    isHex = (root.register(validate_hex), '%P')
    ciphertext_entry = tk.Entry(frame, validate="key", validatecommand=isHex)
    ciphertext_entry.grid(row=0, column=1, padx=10, pady=10)

    key1_label = tk.Label(frame, text="Key 1:")
    key1_label.grid(row=1, column=0, padx=10, pady=10)
    key1_entry = tk.Entry(frame, validate='key', validatecommand=isHex)
    key1_entry.grid(row=1, column=1, padx=10, pady=10)

    key2_label = tk.Label(frame, text="Key 2:")
    key2_label.grid(row=2, column=0, padx=10, pady=10)
    key2_entry = tk.Entry(frame, validate='key', validatecommand=isHex)
    key2_entry.grid(row=2, column=1, padx=10, pady=10)

    key3_label = tk.Label(frame, text="Key 3:")
    key3_label.grid(row=3, column=0, padx=10, pady=10)
    key3_entry = tk.Entry(frame, validate='key', validatecommand=isHex)
    key3_entry.grid(row=3, column=1, padx=10, pady=10)

    trigger = tk.Button(root, text="Encrypt", command=handle_encryption)
    trigger.grid(row=0, column=3, padx=10, pady=10)
    ciphertext_entry.bind("<Return>", lambda event: handle_encryption())

    output = tk.Text(root, height=32, width=40, state=DISABLED)  
    output.grid(row=0, column=5)


    root.mainloop