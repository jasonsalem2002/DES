import tkinter as tk
from tkinter import *
from functions.utils import validate_hex
from encryptionFunctions.Triple_DES_encryption import triple_des_encrypt

def encrypt_triple_des():

    root = Tk.tk()
    root.title("Encrypt Triple DES")
    root.geometry("800x600")

    # add button that triggers key generation later


    root.mainloop