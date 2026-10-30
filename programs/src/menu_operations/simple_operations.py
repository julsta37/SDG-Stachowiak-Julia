import tkinter as tk
from tkinter import filedialog

from src.data_service import get_layer


def simple_operations():
    layer = get_layer()

    if layer is None:
        return

    window = tk.Toplevel()
    window.title("Proste operacje")
    window.geometry("400x300")

    operation = tk.StringVar(value="buffer")
    threshold = tk.StringVar()

    tk.Label(window, text="Operacja:").pack()

    tk.OptionMenu(
        window,
        operation,
        "buffer",
        "convex hull",
        "simplify",
        "centroid"
    ).pack()

    tk.Label(window, text="Threshold:").pack()
    tk.Entry(window, textvariable=threshold).pack()

    def execute():
        value = float(threshold.get())

        result = layer.copy()
        
        if operation.get() == "buffer":
            result["geometry"] = layer.geometry.buffer(value)

        elif operation.get() == "convex hull":
            result["geometry"] = layer.geometry.convex_hull

        elif operation.get() == "simplify":
            result["geometry"] = layer.geometry.simplify(value)

        elif operation.get() == "centroid":
            result["geometry"] = layer.geometry.centroid

        path = filedialog.asksaveasfilename(
            defaultextension=".geojson",
            filetypes=[("GeoJSON", "*.geojson")]
        )

        if path:
            result.to_file(path)
            window.destroy()

    tk.Button(
        window,
        text="Wykonaj",
        command=execute
    ).pack()