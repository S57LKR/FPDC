import tkinter as tk
from tkinter import ttk

import tables
import handle_bom
import handle_pnp
import export
import errors

from tkinter import filedialog
from pathlib import Path


def printSelectedRows(tb):
    selected_rows = tb.selection()
    for row in selected_rows:
        values = tb.item(row, "values")
        print(values)



# Glavno okno
okno = tk.Tk()
okno.title("FPDC v1.0.0 | S57LKR")
okno.geometry("500x700")
okno.resizable(False, False)


# Tabela 1 - BOM
tabela1, okvir1 = tables.createBomTable(okno)
okvir1.place(x=10, y=110)

label_table1 = tk.Label(okno, text="Bill of material:")
label_table1.place(x=10, y=80)

# Tabela 2 - PNP
tabela2, okvir2 = tables.createPnpTable(okno)
okvir2.place(x=10, y=290)

label_table2 = tk.Label(okno, text="Pick and place:")
label_table2.place(x=10, y=260)


tabela3, okvir3 = tables.createExportTable(okno)
okvir3.place(x=10, y=540)

label_table3 = tk.Label(okno, text="Select export:")
label_table3.place(x=10, y=515)

def selectAll():
    tabela3.selection_set(tabela3.get_children())

def unselectAll():
    tabela3.selection_remove(tabela3.selection())


# Gumba
gumb1 = tk.Button(
    okno,
    text="BOM file (.csv)",
    command=lambda: handle_bom.getBomFile(tabela1, label1, handle_pnp.podatki, tabela3)
)
gumb1.place(x=10, y=10)

label1 = tk.Label(okno, text="No file selected")
label1.place(x=10, y=45)


gumb2 = tk.Button(
    okno,
    text="PNP Top (.txt)",
    command=lambda: handle_pnp.getPnpFileTop(tabela2, label2, handle_bom.podatki, tabela3)
)
gumb2.place(x=230, y=10)

label2 = tk.Label(okno, text="No file selected")
label2.place(x=230, y=45)

gumb3 = tk.Button(
    okno,
    text="PNP Bottom (.txt)",
    command=lambda: handle_pnp.getPnpFileBtm(tabela2, label4, handle_bom.podatki, tabela3)
)
gumb3.place(x=350, y=10)

label4 = tk.Label(okno, text="No file selected")
label4.place(x=270, y=45)


# Vodoravna črta
crta = ttk.Separator(okno, orient="horizontal")
crta.place(x=10, y=75, width=480)

crta2 = ttk.Separator(okno, orient="horizontal")
crta2.place(x=10, y=460, width=480)

label3 = tk.Label(okno, text="Export options")
label3.place(x=205, y=450)

selet_all_btn = tk.Button(
    okno,
    text="Select all",
    command=selectAll
)
selet_all_btn.place(x=10, y= 480)

unselet_all_btn = tk.Button(
    okno,
    text="Unselect all",
    command=unselectAll
)
unselet_all_btn.place(x=70, y= 480)

path_lable = tk.Label(
    okno,
    text="No folder selected",
    wraplength=140
)
path_lable.place(x=310, y=510)

select_path_btn = tk.Button(
    okno,
    width=20,
    text="Output file location",
    command=lambda: export.getFilePath(path_lable)
)
select_path_btn.place(x=310, y= 480)

file_name_entry = tk.Entry(
    okno, 
    width=21,
    font=("Arial", 10)
)
file_name_entry.place(x=310, y=585)

file_name_lable = tk.Label(
    okno,
    text="Export file name:"
)
file_name_lable.place(x=310, y=560)


export_btn = tk.Button(
    okno,
    width=20,
    text="Export",
    command=lambda: export.expertFiles((handle_pnp.match_bom or handle_bom.match_bom), (handle_pnp.match_pnp or handle_bom.match_pnp), tabela3, (export.folder or ""), file_name_entry.get(), okno)
)
export_btn.place(x=310, y=620)


okno.mainloop()