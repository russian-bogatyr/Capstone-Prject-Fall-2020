# Test program to demonstrate JPG image display in tkinter.
# PIL needs to be downloaded for this to work.

import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Test Image")
window.geometry("300x300")
window.configure(background="grey")

path = "Sample faces/21_1_2_20170104020235605.jpg.chip.jpg"

img = ImageTk.PhotoImage(Image.open(path))

panel = tk.Label(window, image = img)

panel.pack(side = "bottom", fill = "both", expand = "yes")

window.mainloop()
