import tkinter as tk
from tkinter import filedialog

from src.data_service import get_layer


def simple_operations():
    layer = get_layer()

    if layer is None:
        return

    window = tk.Toplevel()
    window.title("Proste operacje")
    window.geometry("400x350")

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

    threshold_frame = tk.Frame(window)
    tk.Label(threshold_frame, text="Threshold:").pack()
    tk.Entry(threshold_frame, textvariable=threshold).pack()
    threshold_description = tk.Label(
        threshold_frame,
        wraplength=360,
        justify="left"
    )
    threshold_description.pack(pady=5)

    def update_threshold_visibility(*_):
        selected_operation = operation.get()

        if selected_operation in ("buffer", "simplify"):
            if selected_operation == "buffer":
                threshold_description.config(
                    text=(
                        "Buffer: odległość, o jaką geometria zostanie "
                        "powiększona lub pomniejszona, wyrażona w jednostkach "
                        "układu współrzędnych."
                    )
                )
            else:
                threshold_description.config(
                    text=(
                        "Simplify: tolerancja upraszczania geometrii. "
                        "Większa wartość może usunąć więcej szczegółów. "
                        "Wartość jest wyrażona w jednostkach układu współrzędnych."
                    )
                )
            threshold_frame.pack()
        else:
            threshold_frame.pack_forget()

    operation.trace_add("write", update_threshold_visibility)
    update_threshold_visibility()

    def execute():
        result = layer.copy()
        
        if operation.get() == "buffer":
            result["geometry"] = layer.geometry.buffer(float(threshold.get()))

        elif operation.get() == "convex hull":
            result["geometry"] = layer.geometry.convex_hull

        elif operation.get() == "simplify":
            result["geometry"] = layer.geometry.simplify(float(threshold.get()))

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
