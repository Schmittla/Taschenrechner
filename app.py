# ===================================================================
# Mini-Rechner Anwendung mit Tkinter
# ===================================================================
# Diese Anwendung erstellt einen einfachen grafischen Taschenrechner,
# der die vier Grundrechenarten (Addition, Subtraktion, Multiplikation
# und Division) unterstützt.
# ===================================================================

# Import des tkinter-Moduls für die grafische Benutzeroberfläche (GUI)
import tkinter as tk


# -----------------------------
# Funktionen
# -----------------------------
def add_to_display(value):
    """Fügt eine Zahl oder einen Operator zum Display hinzu"""
    display.insert(tk.END, value)


def calculate():
    """Berechnet den Ausdruck im Display"""
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Fehler")


def clear_display():
    """Löscht das Display"""
    display.delete(0, tk.END)


# -----------------------------
# Hauptfenster
# -----------------------------
root = tk.Tk()
root.title("Taschenrechner")
root.geometry("320x420")
root.resizable(False, False)


# -----------------------------
# Display
# -----------------------------
display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief=tk.RIDGE
)
display.pack(fill="x", padx=10, pady=10)


# -----------------------------
# Button-Layout
# -----------------------------
button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Grid-Konfiguration (Buttons gleich groß)
for i in range(5):
    button_frame.rowconfigure(i, weight=1)
for j in range(4):
    button_frame.columnconfigure(j, weight=1)

# -----------------------------
# Buttons erzeugen
# -----------------------------
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 18),
            command=calculate
        )
    else:
        btn = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 18),
            command=lambda t=text: add_to_display(t)
        )

    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# -----------------------------
# Clear-Button
# -----------------------------
clear_btn = tk.Button(
    root,
    text="C",
    font=("Arial", 18),
    bg="lightcoral",
    command=clear_display
)
clear_btn.pack(fill="x", padx=10, pady=5)


# -----------------------------
# Event-Loop starten
# -----------------------------
root.mainloop()