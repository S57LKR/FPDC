import tkinter as tk
from tkinter import ttk

def showMessage(okno, tt,  message):
    msg = tk.Toplevel(okno)
    msg.title(tt)
    msg.geometry("300x120")
    msg.resizable(False, False)

    label = tk.Label(msg, text=message, wraplength=270)
    label.pack(pady=15)

    btn = tk.Button(msg, text="OK", width=10, command=msg.destroy)
    btn.pack()

    msg.grab_set()

eror_list = [
    ["Save fille name missing", "Enter file name"],
    ["Invalid characterts in file name", "Invalid characters: \\/:*?<>|.[space]"],
    ["Creating BOM file failed", "Try again or change parameters"],
    ["Program has no permision to create new .xlsx file", "Give permission in settings"],
]

def showError(okno, ecd):
    msg = tk.Toplevel(okno)
    msg.title("Error - FPDC")
    msg.geometry("300x120")
    msg.resizable(False, False)

    label = tk.Label(msg, text=eror_list[ecd][0], wraplength=270)
    label.pack(pady=15)
    label2 = tk.Label(msg, text=eror_list[ecd][1], wraplength=270)
    label2.pack(pady=15)

    btn = tk.Button(msg, text="OK", width=10, command=msg.destroy)
    btn.pack()

    msg.grab_set()