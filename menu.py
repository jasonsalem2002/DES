import tkinter as tk
from tkinter import messagebox
from tkinter import *
from functions.utils import keyGeneration
from encryptionFunctions.DES_encryption import encrypt
from decryptionFunctions.DES_decryption import decrypt
from functions.utils import validate_hex
from pages.encrypt_des_page import encrypt_des_test
from pages.decrypt_des_page import decrypt_des_test
from tkinter import ttk
#from pages.encrypt_3des_page import encrypt_triple_des

# might delete later
# used to animate gif
def update_background(canvas, images, index):
    canvas.itemconfig(background_image, image=images[index])
    index = (index + 1) % len(images)
    canvas.after(100, update_background, canvas, images, index)


def main():
    root = tk.Tk()
    root.title("DES-TripleDES")
    root.geometry("400x500")
    root.maxsize(800, root.winfo_screenheight())

    # for the gif background
    # fina nshilo baaden iza ktir beshe3
    canvas = tk.Canvas(root)
    canvas.pack(fill=tk.BOTH, expand=True)
    images = [tk.PhotoImage(file=f"media/background_{i}.gif") for i in range(0, 4)]
    global background_image
    background_image = canvas.create_image(0, 0, anchor=tk.NW, image=images[0])
    update_background(canvas, images, 0)

    color1 = '#00FF00'
    color2 = '#149414'
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
    # i want a 2x2 grid
    # Configure columns
    for col in range(2):
        frame.columnconfigure(col, weight=1, minsize=100)
    for row in range(2):
        frame.rowconfigure(row, weight=1, minsize=100)

    # style = ttk.Style()
    # style.configure(
    #     'Custom.TButton', 
    #     background=color2, 
    #     foreground=color4, 
    #     activebackground=color3, 
    #     activeforeground=color4,
    #     font=('Courier', 10, 'bold'), 
    #     highlightbackground=color2,
    #     highlightcolor='WHITE', 
    #     width=7, 
    #     height=7,
    #     border=0,
    #     cursor='cross')

    # encrypt_des_button = ttk.Button(
    #     frame,
    #     text="Encrypt (DES)",
    #     style='Custom.TButton',
    #     command=encrypt_des_test
    # )

    encrypt_des_button = tk.Button(
        frame,
        background=color2,
        foreground=color4,
        activebackground=color3,
        activeforeground=color4,
        highlightthickness=2,
        highlightbackground=color2,
        highlightcolor='WHITE',
        width=7,
        height=7,
        border=0,
        cursor='cross',
        text="Encrypt (DES)", 
        font=('Courier', 10, 'bold'),
        command=encrypt_des_test)
    encrypt_des_button.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')


    decrypt_des_button = tk.Button(
        frame, 
        background=color2,
        foreground=color4,
        activebackground=color3,
        activeforeground=color4,
        highlightcolor='WHITE',
        width=7,
        height=7,
        cursor='cross',
        border=0,
        text="Decrypt (DES)",
        font=('mechanical', 10, 'bold'),
        command=decrypt_des_test)
    decrypt_des_button.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')


    encrypt_3des_button = tk.Button(
        frame, 
        background=color2,
        width=7,
        height=7,
        cursor='cross',
        border=0,
        text="Encrypt (Triple DES)",
        font=("mechanical", 10, 'bold')
        #command=encrypt_triple_des
        ) # changed decrypt_des to decrypt
    encrypt_3des_button.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')


    decrypt_3des_button = tk.Button(
        frame,
        background=color2,
        width=7,
        height=7,
        cursor='cross',
        border=0,
        text="Decrypt (Triple DES)", 
        font=("mechanical", 10, 'bold')
        #command=decrypt_des
        )
    decrypt_3des_button.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')


    root.mainloop()

if __name__ == "__main__":
    main()
