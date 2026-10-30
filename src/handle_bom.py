import csv
from tkinter import filedialog
from pathlib import Path
import find_match

podatki = []
match_pnp = []
match_bom = []


def getBomFile(tabela1, label1, pnpf, mt):
    global podatki
    global match_pnp, match_bom

    csv_datoteka = filedialog.askopenfilename(
        title="Izberi BOM datoteko",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )

    if not csv_datoteka:
        return

    podatki.clear()
    tabela1.delete(*tabela1.get_children())

    with open(csv_datoteka, "r", encoding="utf-8-sig",
              errors="replace", newline="") as f:

        reader = csv.DictReader(f, delimiter=";")

        for vrstica in reader:
            reference = vrstica.get("Reference Designators", "").strip()

            if reference.startswith("///////////XMLX"):
                break

            if not reference:
                continue

            comment = (
                vrstica.get("Value", "").strip()
                or vrstica.get("Manufacturer Part Number", "").strip()
                or vrstica.get("Description", "").strip()
            )

            footprint = vrstica.get("Package", "").strip()
            lcsc_part = vrstica.get("LCSC Part #", "").strip()

            podatki.append([
                comment,
                reference,
                footprint,
                lcsc_part
            ])

    for row in podatki:
        tabela1.insert("", "end", values=(row[1], row[0], row[2]))

    label1.config(text=Path(csv_datoteka).name)

    if len(pnpf) > 0:
        match_pnp, match_bom = find_match.findMatchComponents(pnpf, podatki, mt)
        print(match_pnp[0] or "invalid data")

    print("BOM naložen:", len(podatki), "vrstic")