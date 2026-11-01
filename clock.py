"""A small digital clock built with Python's standard-library Tkinter."""

import tkinter as tk
from time import strftime


def update_clock() -> None:
    clock_label.config(text=strftime("%I:%M:%S %p"))
    clock_label.after(1000, update_clock)


window = tk.Tk()
window.title("Digital Clock")
window.geometry("360x140")
window.resizable(False, False)
window.configure(bg="#1e1e1e")

clock_label = tk.Label(
    window,
    font=("Arial", 40, "bold"),
    background="#1e1e1e",
    foreground="#00ff99",
)
clock_label.pack(expand=True)

update_clock()
window.mainloop()