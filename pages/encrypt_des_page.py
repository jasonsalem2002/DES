import tkinter as tk
from tkinter import *
from functions.utils import validate_hex, keyGeneration
from encryptionFunctions.DES_encryption import encrypt
from functions.randomKeyGenerator import generate_random_key

def encrypt_des_test():

    global output 

    def handle_encryption(event=None):
        plaintext=plaintext_entry.get()
        key=key_entry.get()
        if (plaintext and key):
            rkb = keyGeneration(key)
            rk = [format(int(keyR, 2), '012X') for keyR in rkb]
            ciphertext = encrypt(plaintext, rkb, rk)
            output.config(state="normal")  # Set state to normal to allow editing temporarily
            output.delete('1.0', tk.END)  # Clear previous content
            output.insert(tk.END, ciphertext)
            output.config(state="disabled")  # Set state back to disabled after inserting ciphertext

    root = tk.Tk()
    root.title("Encrypt DES")
    root.geometry("800x600")

    # label for plaintext input box
    plaintext_label = tk.Label(root, text="plaintext")
    plaintext_label.grid(row=0, column=0, padx=10, pady=10)
    # defining the function to validate if hex
    isHex = (root.register(validate_hex), '%P')
    plaintext_entry = tk.Entry(root, validate="key", validatecommand=isHex)
    plaintext_entry.grid(row=0, column=1, padx=10, pady=10)
    
    key_label = tk.Label(root, text="Key:")
    key_label.grid(row=1, column=0, padx=10, pady=10)
    key_entry = tk.Entry(root, validate='key', validatecommand=isHex)
    key_entry.grid(row=1, column=1, padx=10, pady=10)

    # random key generation
    frame = tk.Frame(root, width=200, height=100, bg="lightblue")
    frame.grid(row=3, column=8)

    random_key_var = tk.StringVar()
    
    def get_rand_key():
        generated_key = generate_random_key()
        #key_label.grid(row=1, column=1)
        #key_label.config(text="Random Key: " + generated_key)
        random_key_var.set(generated_key)
        return generated_key

    randKey_label = tk.Label(frame, text="Generate random key")
    randKey_label.grid(row=0, column=0, padx=5, pady=5)
    randKey_button = tk.Button(frame, text="Generate", command=get_rand_key)
    randKey_button.grid(row=0, column=1, padx=5, pady=5)
    generated_key_label = tk.Label(frame, textvariable=random_key_var)
    generated_key_label.grid(row=1, column=0, padx=5, pady=5)
    frame.columnconfigure(0, weight=1)

    # encryption should be triggered by either ENTER or clicking button
    trigger = tk.Button(root, text="Encrypt", command=handle_encryption)
    trigger.grid(row=0, column=4, padx=10, pady=10)
    plaintext_entry.bind("<Return>", lambda event: handle_encryption())

    output = tk.Text(root, height=32, width=40, state=DISABLED)  
    output.grid(row=3, column=0)

    root.mainloop()