import tkinter as tk
from tkinter import ttk


def createBomTable(parent):
    okvir = tk.Frame(parent, width=480, height=150)
    okvir.pack_propagate(False)

    stolpci = ("1", "2", "3")

    tabela = ttk.Treeview(
        okvir,
        columns=stolpci,
        show="headings",
        height=6
    )

    tabela.heading("1", text="Des")
    tabela.heading("2", text="Value")
    tabela.heading("3", text="Fp")

    tabela.column("1", width=100)
    tabela.column("2", width=60)
    tabela.column("3", width=60)

    scrollbar = ttk.Scrollbar(
        okvir,
        orient="vertical",
        command=tabela.yview
    )

    tabela.configure(yscrollcommand=scrollbar.set)

    tabela.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return tabela, okvir


def createPnpTable(parent):
    okvir = tk.Frame(parent, width=480, height=150)
    okvir.pack_propagate(False)

    stolpci = ("1", "2", "3", "4", "5")

    tabela = ttk.Treeview(
        okvir,
        columns=stolpci,
        show="headings",
        height=6
    )

    tabela.heading("1", text="Des")
    tabela.heading("2", text="Mid X")
    tabela.heading("3", text="Mid Y")
    tabela.heading("4", text="Angle")
    tabela.heading("5", text="Layer")

    tabela.column("1", width=40)
    tabela.column("2", width=50)
    tabela.column("3", width=50)
    tabela.column("4", width=50)
    tabela.column("5", width=50)

    scrollbar = ttk.Scrollbar(
        okvir,
        orient="vertical",
        command=tabela.yview
    )

    tabela.configure(yscrollcommand=scrollbar.set)

    tabela.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return tabela, okvir

def createExportTable(parent):
    okvir = tk.Frame(parent, width=200, height=150)
    okvir.pack_propagate(False)

    stolpci = ("1", "2", "3", "4")

    tabela = ttk.Treeview(
        okvir,
        columns=stolpci,
        show="headings",
        height=6
    )

    tabela.heading("1", text="Des")
    tabela.heading("2", text="Value")
    tabela.heading("3", text="Layer")
    tabela.heading("4", text="Index")


    tabela.column("1", width=40)
    tabela.column("2", width=60)
    tabela.column("3", width=60)
    tabela.column("4", width=0, minwidth=0, stretch=False)

    scrollbar = ttk.Scrollbar(
        okvir,
        orient="vertical",
        command=tabela.yview
    )

    tabela.configure(yscrollcommand=scrollbar.set)

    tabela.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    return tabela, okvir