from pathlib import Path
import tkinter as tk

# Definicje metod:

def close_program():
    window.destroy()


# Utworzenie głównego okna + canvas:

window = tk.Tk()
window.title("Baza Geoinfo")
window.resizable(False, False)

canvas = tk.Canvas(
    window,
    width=650,
    height=550,
    highlightthickness=0
)

canvas.pack()


# Grafika tła:

image_path = Path(__file__).resolve().with_name("ekran.png")
background_screen = tk.PhotoImage(file=str(image_path))

canvas.create_image(
    0,
    0,
    image=background_screen,
    anchor="nw"
)


# Tytuł programu:
canvas.create_text(
    200,
    50,
    text="Baza Geoinfo",
    font=("Arial", 30, "bold"),
    fill="white"
)


# Menu:

canvas.create_text(
    180,
    420,
    text="Wybierz operację:",
    font=("Arial", 16, "bold"),
    fill="white"
)


# Przycisk zamknięcia:

canvas.create_text(
    180,
    465,
    text="Zamknij program",
    font=("Arial", 11, "bold"),
    fill="white",
    tags="zamknij"
)

canvas.tag_bind(
    "zamknij",
    "<Button-1>",
    lambda event: close_program()
)

canvas.tag_bind(
    "zamknij",
    "<Enter>",
    lambda event: canvas.itemconfig(
        "zamknij",
        fill="#90E0EF"
    )
)

canvas.tag_bind(
    "zamknij",
    "<Leave>",
    lambda event: canvas.itemconfig(
        "zamknij",
        fill="white"
    )
)

# Główna pętla programu:

window.mainloop()
