from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"

FRAME_THICKNESS = 10

# Kolory
COLOUR_PALETTE = ["#F0F0F0", "#213555", "#4F709C", "#E5D283"]



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Typing Speed Test")
window.config(padx=100, pady=50, bg=COLOUR_PALETTE[0])

title = Label(text="Typing Speed Test", font=(FONT_NAME, 35), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[1])
title.grid(column=0, row=0, columnspan=2)

with Image.open("Keyboard-front.jpg") as image:
    img_width = image.width
    img_height = image.height
    ratio = 7
    # Utworzenie miniatury do poglądu
    image.thumbnail((img_width / ratio, img_height / ratio))
    # Utworzenie ramki
    photo_with_frame = ImageOps.expand(image, border=FRAME_THICKNESS, fill=COLOUR_PALETTE[2])
    photo = ImageTk.PhotoImage(photo_with_frame)
    # Przypisanie miniatury do etykiety
    picture = Label(image=photo)
    picture.grid(column=0, row=2, columnspan=2, pady=25)


window.mainloop()
