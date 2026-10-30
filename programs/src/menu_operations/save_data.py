from tkinter import filedialog, messagebox

from src.data_service import get_layer


def save_data():
    layer = get_layer()

    if layer is None:
        return

    path = filedialog.asksaveasfilename(
        title="Zapisz warstwę",
        defaultextension=".geojson",
        filetypes=[
            ("GeoJSON", "*.geojson"),
            ("GeoPackage", "*.gpkg"),
            ("Shapefile", "*.shp"),
            ("CSV", "*.csv")
        ]
    )

    if not path:
        return

    try:
        if path.endswith(".csv"):
            layer.to_csv(path, index=False, sep=",", encoding="utf-8")
        else:
            layer.to_file(path)

        messagebox.showinfo(
            "Zapisano plik",
            "Warstwa została zapisana poprawnie."
        )

    except Exception:
        messagebox.showwarning(
            "Błąd zapisu",
            "Nie udało się zapisać warstwy."
        )
