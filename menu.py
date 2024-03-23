import tkinter as tk
from tkinter import messagebox
from tkinter import *
from functions.utils import keyGeneration
from encryptionFunctions.DES_encryption import encrypt
from decryptionFunctions.DES_decryption import decrypt
from functions.utils import validate_hex
from pages.encrypt_des_page import encrypt_des_test
from pages.decrypt_des_page import decrypt_des_test

# might delete later
# used to animate gif
def update_background(canvas, images, index):
    canvas.itemconfig(background_image, image=images[index])
    index = (index + 1) % len(images)
    canvas.after(100, update_background, canvas, images, index)


# def encrypt_des():
#     root = tk.Tk()
#     root.title("Encrypt DES")
#     root.geometry("400x500")

#     # defining the function to validate if hex
#     isHex = (root.register(validate_hex), '%P')
#     plaintext_entry = tk.Entry(root, validate="key", validatecommand=isHex)
#     plaintext_entry.pack()

#     # getting the entry
#     plaintext=plaintext_entry.get()
#     # pressing ENTER should trigger the encryption (not working rn)
#     plaintext_entry.bind("<Return>", encrypt)
#     #plaintext = "123456ABCD132536"
#     key = "AABB09182736CCDD"
#     rkb = keyGeneration(key)
#     rk = [] 
#     for keyR in rkb:
#         rk.append(format(int(keyR, 2), '012X'))
#     ciphertext = encrypt(plaintext, rkb, rk)

#     output.config(text=ciphertext)
#     output.pack() # ERROR - nothing is displaying on this window except the input box
    
#     label = tk.Label(root, text="test test test")
#     label.pack()
#     # messagebox.showinfo("DES Encryption", ciphertext)

#     root.mainloop()


# def decrypt_des():
#     cipher = "C0B7A8D05F3A829C"
#     key = "AABB09182736CCDD"
#     decrypted = decrypt(cipher, key)
#     messagebox.showinfo("DES Decryption", decrypted)


def main():
    root = tk.Tk()
    root.title("DES-TripleDES")
    root.geometry("400x500")

    # for the gif background
    # fina nshilo baaden iza ktir beshe3
    canvas = tk.Canvas(root)
    canvas.pack(fill=tk.BOTH, expand=True)
    images = [tk.PhotoImage(file=f"media/background_{i}.gif") for i in range(0, 4)]
    global background_image
    background_image = canvas.create_image(0, 0, anchor=tk.NW, image=images[0])
    update_background(canvas, images, 0)

    color1 = '#00FF00'
    color2 = '#ADFF2F'
    color3 = '#138A36'
    color4 = 'BLACK'

    # using frames - maybe easier to switch from frame to frame instead of opening new windows
    frame = tk.Frame(
        root, 
        bg=color4, 
        padx=20, 
        pady=20)
    frame.pack(fill=tk.BOTH, expand=True)
    # label_frame = tk.Label(frame, text="test", bg="white")
    # label_frame.pack(padx=10, pady=10)
    # use this later to add how many columns i want in the frame
    # frame.columnconfigure()
    # frame.rowconfigure()


    encrypt_des_button = tk.Button(
        frame,
        background=color2,
        foreground=color4,
        activebackground=color3,
        activeforeground=color4,
        highlightthickness=2,
        highlightbackground=color2,
        highlightcolor='WHITE',
        # width
        # height
        border=0,
        cursor='cross',
        text="Encrypt (DES)", 
        font=('courier', 16, 'bold'),
        command=encrypt_des_test)
    encrypt_des_button.pack(pady=5)


    decrypt_des_button = tk.Button(frame, text="Decrypt (DES)", command=decrypt_des_test)
    decrypt_des_button.pack(pady=5)


    # enrypt_3des_button = tk.Button(frame, text="Encrypt (Triple DES)", command=decrypt) # changed decrypt_des to decrypt
    # encrypt_3des_button.pack(pady=5)


    # decrypt_3des_button = tk.Button(frame, text="Decrypt (Triple DES)", command=decrypt_des)
    # decrypt_3des_button.pack(pady=5)


    root.mainloop()

if __name__ == "__main__":
    main()
