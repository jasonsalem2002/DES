import tkinter as tk
from tkinter import *
from tkinter import messagebox
from functions.utils import validate_hex, keyGeneration
from decryptionFunctions.DES_decryption import decrypt

def decrypt_des_test():

    global output

    root = tk.Tk()
    root.title("Decrypt DES")
    root.geometry("800x600")

    isHex = (root.register(validate_hex), '%P')

    def handle_decryption(event=None):
        ciphertext = ciphertext_entry.get()
        key = key_entry.get()
        if len(ciphertext) != 16:
            messagebox.showerror("Error", "Ciphertext must be exactly 16 characters long.")
            return
        if len(key) != 16:
            messagebox.showerror("Error", "Key must be exactly 16 characters long.")
            return # dont need to validate if input is not empty after this
        if (ciphertext and key):
            keyB = keyGeneration(key)
            plaintext = decrypt(ciphertext, keyB)
            output.config(state="normal")  
            output.delete('1.0', tk.END) 
            output.insert(tk.END, plaintext)
            output.config(state="disabled")


    ciphertext_label = tk.Label(root, text="Ciphertext:")
    ciphertext_label.grid(row=0, column=0, padx=10, pady=10)
    ciphertext_entry = tk.Entry(root, validate="key", validatecommand=isHex)
    ciphertext_entry.grid(row=0, column=1, padx=10, pady=10)

    key_label = tk.Label(root, text="Key:")
    key_label.grid(row=1, column=0, padx=10, pady=10)
    key_entry = tk.Entry(root, validate='key', validatecommand=isHex)
    key_entry.grid(row=1, column=1, padx=10, pady=10)

    trigger = tk.Button(root, text="Decrypt", command=handle_decryption)
    trigger.grid(row=0, column=4, padx=10, pady=10)
    ciphertext_entry.bind("<Return>", lambda event: handle_decryption())

    output = tk.Text(root, height=32, width=40, state=DISABLED)  
    output.grid(row=3, column=0)

    root.mainloop()


