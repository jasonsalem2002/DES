import tkinter as tk
from tkinter import *
from tkinter import messagebox
from functions.utils import validate_hex, keyGeneration
from encryptionFunctions.Triple_DES_encryption import triple_des_encrypt
from functions.randomKeyGenerator import generate_random_key

def encrypt_triple_des():

    root = tk.Tk()
    root.title("Encrypt Triple DES")
    root.geometry("800x600")

    global output

    def handle_encryption(event=None):
        plaintext=plaintext_entry.get()
        key1 = key1_entry.get()
        key2 = key2_entry.get()
        key3 = key3_entry.get()

        if len(plaintext) != 16:
            messagebox.showerror("Error", "Plaintext must be exactly 16 characters long.")
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
        ciphertext = triple_des_encrypt(plaintext, keyb, triple_des_keys)
        output.config(state="normal")
        output.delete('1.0', tk.END)
        output.insert(tk.END, ciphertext)
        output.config(state="disabled")


    frame = tk.Frame(root)
    frame.grid(row=0, column=0, rowspan=5, columnspan=3)

    def get_rand_key():
        global generated_key 
        generated_key = generate_random_key()
        if len(key1_entry.get()) == 0:
            key1_entry.delete(0, last=None)
            key1_entry.insert(0, generated_key)
        elif len(key2_entry.get()) == 0:
            key2_entry.delete(0, last=None)
            key2_entry.insert(0, generated_key)
        elif len(key3_entry.get()) == 0:
            key3_entry.delete(0, last=None)
            key3_entry.insert(0, generated_key)
        else:
            return

    plaintext_label = tk.Label(frame, text="plaintext")
    plaintext_label.grid(row=0, column=0, padx=10, pady=10)
    isHex = (root.register(validate_hex), '%P')
    plaintext_entry = tk.Entry(frame, validate="key", validatecommand=isHex)
    plaintext_entry.grid(row=0, column=1, padx=10, pady=10)

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

    randKey_button = tk.Button(frame, text="Generate Random Key", command=get_rand_key)
    randKey_button.grid(row=4, column=0, padx=5, pady=5)

    trigger = tk.Button(root, text="Encrypt", command=handle_encryption)
    trigger.grid(row=0, column=3, padx=10, pady=10)
    plaintext_entry.bind("<Return>", lambda event: handle_encryption())

    output = tk.Text(root, height=32, width=40, state=DISABLED)  
    output.grid(row=0, column=5)


    root.mainloop