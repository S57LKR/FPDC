from tkinter import filedialog
from pathlib import Path
import find_match



podatki = []
match_pnp = []
match_bom = []


def getPnpFileTop(tabela2, label2, bmf, mt):
    global match_pnp, match_bom
    global podatki

    input_file = filedialog.askopenfilename(
        title="Izberi PnP datoteko",
        filetypes=[
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ]
    )

    if not input_file:
        return

    with open(input_file, "r", encoding="utf-8-sig",
              errors="replace") as file:

        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split()

            if len(parts) != 6:
                print("Preskakujem neveljavno vrstico:", line)
                continue

            designator, x, y, rotation, comment, footprint = parts

            try:
                x = float(x)
                y = float(y)
                rotation = float(rotation)
            except ValueError:
                print("Neveljavne številčne vrednosti:", line)
                continue

            podatki.append([
                designator,
                x,
                y,
                rotation,
                comment,
                footprint,
                "Top"
            ])

    for row in podatki:
        tabela2.insert(
            "",
            "end",
            values=(row[0], row[1], row[2], row[3], row[6])
        )

    label2.config(text=Path(input_file).name)

    if len(bmf) > 0:
        match_pnp, match_bom = find_match.findMatchComponents(bmf, podatki, mt)
        print(match_pnp[0] or "invalid data")
    

    print("PnP naložen:", len(podatki), "vrstic")


def getPnpFileBtm(tabela2, label2, bmf, mt):
    global podatki
    global match_pnp, match_bom

    input_file = filedialog.askopenfilename(
        title="Izberi PnP datoteko",
        filetypes=[
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ]
    )

    if not input_file:
        return

    with open(input_file, "r", encoding="utf-8-sig",
              errors="replace") as file:

        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split()

            if len(parts) != 6:
                print("Preskakujem neveljavno vrstico:", line)
                continue

            designator, x, y, rotation, comment, footprint = parts

            try:
                x = float(x)
                y = float(y)
                rotation = float(rotation)
            except ValueError:
                print("Neveljavne številčne vrednosti:", line)
                continue

            podatki.append([
                designator,
                x,
                y,
                rotation,
                comment,
                footprint,
                "Bottom"
            ])

    for row in podatki:
        tabela2.insert(
            "",
            "end",
            values=(row[0], row[1], row[2], row[3], row[6])
        )


    if len(bmf) > 0:
        match_pnp, match_bom = find_match.findMatchComponents(bmf, podatki, mt)
        print(match_pnp[0] or "invalid data")


    print("PnP naložen:", len(podatki), "vrstic")