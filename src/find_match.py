from tkinter import filedialog
from pathlib import Path
import inspect

def findMatchComponents(bom, pnp, mt):

    match_pnp = []
    match_bom = []

    for i in range(len(pnp)):
        des = pnp[i][0]

        for j in range(len(bom)):
            if des in bom[j][1]:

                match_pnp.append(pnp[i])

                val = bom[j][0]
                fp = bom[j][2]

                found = False

                for k in range(len(match_bom)):
                    if val == match_bom[k][0] and fp == match_bom[k][2]:
                        match_bom[k][1] += ", " + des
                        found = True
                        break

                if not found:
                    match_bom.append([
                        val,
                        des,
                        fp
                    ])

                break
    i = 0
    for row in match_pnp:
        mt.insert(
            "",
            "end",
            values=(row[0], row[4], row[6], str(i))
        )
        i += 1

    print("\n--- MATCH BOM ---")
    for row in match_bom:
        print(row)

    print("\n--- MATCH PNP ---")
    for row in match_pnp:
        print(row)

    frame = inspect.currentframe().f_back
    print("Datoteka:", frame.f_code.co_filename)
    print("Funkcija:", frame.f_code.co_name)
    print("Vrstica:", frame.f_lineno)

    return match_pnp, match_bom


