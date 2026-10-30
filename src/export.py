
from tkinter import filedialog
from pathlib import Path
import errors
import csv
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
import os


def expertFiles(bom, pnp, tb, le, file_name, okno):
    if file_name == "":
        errors.showError(okno, 0)
        return

    if any(char in file_name for char in '\\/:*?"<>|. '):
        errors.showError(okno, 1)
        return

    if not le:
        errors.showMessage(okno, "Error", "Output folder not selected")
        return

    selected_rows = tb.selection()
    exportPnP = []
    exportBoM = []

    for row in selected_rows:
        values = tb.item(row, "values")
        index = int(values[3])

        exportPnP.append(pnp[index])
        des = pnp[index][0]

        for bom_row in bom:
            if des in [x.strip() for x in bom_row[1].split(",")]:
                val = bom_row[0]
                fp = bom_row[2]

                found = False

                for k in range(len(exportBoM)):
                    if val == exportBoM[k][0] and fp == exportBoM[k][2]:
                        exportBoM[k][1] += ", " + des
                        found = True
                        break

                if not found:
                    exportBoM.append([val, des, fp])

                break

    #----------------------------- create BOM file ---------------------------------

    xlsx_datoteka = os.path.join(le, file_name + "_BOM.xlsx")

    try:
        wb = Workbook()
        ws = wb.active
        ws.title = "BOM"

        glava = ["Comment", "Designator", "Footprint", "LCSC Part #"]
        ws.append(glava)

        for vrstica in exportBoM:
            ws.append(vrstica)

        for celica in ws[1]:
            celica.font = Font(bold=True, color="FFFFFF")
            celica.fill = PatternFill("solid", fgColor="333333")
            celica.alignment = Alignment(horizontal="center")

        for stolpec in ws.columns:
            sirina = max(len(str(c.value or "")) for c in stolpec)
            ws.column_dimensions[get_column_letter(stolpec[0].column)].width = min(sirina + 3, 60)

        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions

        wb.save(xlsx_datoteka)

        if not os.path.isfile(xlsx_datoteka):
            errors.showError(okno, 2)
            return

        print("BOM uspešno ustvarjen:", xlsx_datoteka)

    except PermissionError:
        errors.showError(okno, 3)
        return

    except Exception as e:
        errors.showMessage(okno, "Error - BOM", e)
        return

    #----------------------------- create PNP file ---------------------------------

    xlsx_datoteka = os.path.join(le, file_name + "_PnP.xlsx")

    try:
        wb = Workbook()
        ws = wb.active
        ws.title = "CPL"

        glava = [
            "Designator",
            "Mid X",
            "Mid Y",
            "Layer",
            "Rotation",
            "Comment",
            "Footprint"
        ]

        ws.append(glava)

        for vrstica in exportPnP:
            ws.append([
                vrstica[0],
                float(vrstica[1]),
                float(vrstica[2]),
                vrstica[6],
                float(vrstica[3]),
                vrstica[4],
                vrstica[5]
            ])

        for celica in ws[1]:
            celica.font = Font(bold=True, color="FFFFFF")
            celica.fill = PatternFill(
                "solid", fgColor="4472C4"
            )
            celica.alignment = Alignment(horizontal="center")

        widths = [16, 12, 12, 12, 12, 22, 30]

        for i, width in enumerate(widths, start=1):
            ws.column_dimensions[get_column_letter(i)].width = width

        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions

        wb.save(xlsx_datoteka)

        if not os.path.isfile(xlsx_datoteka):
            errors.showError(okno, 2)
            return

        print("PnP uspešno ustvarjen:", xlsx_datoteka)

    except PermissionError:
        errors.showError(okno, 3)
        return

    except Exception as e:
        errors.showMessage(okno, "Error - PnP", e)
        return

    #-------------------------------------------------------------------------------

    return exportPnP, exportBoM

def getFilePath(lable):
    global folder
    folder = filedialog.askdirectory(title="Izberi mapo za shranjevanje")

    if folder:
        print("Izbrana mapa:", folder)
        lable.config(text=folder)