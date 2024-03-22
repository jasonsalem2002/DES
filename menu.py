import tkinter as tk
from tkinter import messagebox
from functions.utils import keyGeneration
from DES_encryption import encrypt
from DES_decryption import decrypt

def encrypt_des():
    plaintext = "123456ABCD132536"
    key = "AABB09182736CCDD"
    rkb = keyGeneration(key)
    rk = [] 
    for keyR in rkb:
        rk.append(format(int(keyR, 2), '012X'))
    ciphertext = encrypt(plaintext, rkb, rk)
    
    messagebox.showinfo("DES Encryption", ciphertext)

def decrypt_des():
    cipher = "C0B7A8D05F3A829C"
    key = "AABB09182736CCDD"
    decrypted = decrypt(cipher, key)

    messagebox.showinfo("DES Decryption", decrypted)


def main():
    root = tk.Tk()
    root.title("DES-TripleDES")

    encrypt_des_button = tk.Button(root, text="Encrypt (DES)", command=encrypt_des)
    encrypt_des_button.pack(pady=5)

    decrypt_des_button = tk.Button(root, text="Decrypt (DES)", command=decrypt_des)
    decrypt_des_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
