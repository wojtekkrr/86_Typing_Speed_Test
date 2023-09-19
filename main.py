import tkinter
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
from faker import Faker

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"

FRAME_THICKNESS = 10

# Kolory
COLOUR_PALETTE = ["#DDF7E3", "#C7E8CA", "#5D9C59", "#DF2E38", "#000000"]

fake = Faker()
NR_OF_WORDS = 100
RANDOM_WORDS = []
for _ in range(NR_OF_WORDS):
    RANDOM_WORDS.append(fake.word())


# ---------------------------- ACCEPT AFTER SPACE ------------------------------- #
def accept_after_space(event):
    text_generated_label_1.configure(style="Background.TLabel")
    print("tak, działa")
    #     #Tutaj dać generację kolejnego słowa, czy coś



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Typing Speed Test")
window.config(padx=100, pady=50, bg=COLOUR_PALETTE[0])

#Środkowanie zawartości
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

title = Label(text="Typing Speed Test", font=(FONT_NAME, 35), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[2])
title.grid(column=0, row=0, columnspan=2)

with Image.open("Keyboard-front.jpg") as image:
    img_width = image.width
    img_height = image.height
    ratio = 7
    # Utworzenie miniatury do poglądu
    image.thumbnail((img_width / ratio, img_height / ratio))
    # Utworzenie ramki
    photo_with_frame = ImageOps.expand(image, border=FRAME_THICKNESS, fill=COLOUR_PALETTE[1])
    photo = ImageTk.PhotoImage(photo_with_frame)
    # Przypisanie miniatury do etykiety
    picture = Label(image=photo)
    picture.grid(column=0, row=1, columnspan=2, pady=25)

text_label = Label(text="Text", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[4])
text_label.grid(column=0, row=3, pady=25)

# text_generated_label_1 = ttk.Label(text=RANDOM_WORDS[:5], font=(FONT_NAME, 12))
# style = ttk.Style()
# style.configure("Green.TLabel", foreground=COLOUR_PALETTE[2], background=COLOUR_PALETTE[0])
# text_generated_label_1.grid(column=0, row=4)

background_color = COLOUR_PALETTE[0]
style = ttk.Style()
style.configure("Background.TFrame", background="red")
text_generated_frame_1 = ttk.Frame(style="Background.TFrame")
text_generated_frame_1.grid(column=0, row=4)
style.configure("Background.TLabel", background="red")
text_generated_label_1 = ttk.Label(text_generated_frame_1, text=RANDOM_WORDS[:5], font=(FONT_NAME, 12))
text_generated_label_1.grid(column=0, row=4)

text_generated_label_2 = Label(text=RANDOM_WORDS[5:10], font=(FONT_NAME, 12), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[4])
text_generated_label_2.grid(column=0, row=5)

text_generated_label_3 = Label(text=RANDOM_WORDS[10:15], font=(FONT_NAME, 12), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[4])
text_generated_label_3.grid(column=0, row=6)

type_label = Label(text="Type", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[4])
type_label.grid(column=0, row=7, pady=25)

type_entry = Entry(width=40, bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[2], justify="center")
type_entry.grid(column=0, row=8)
type_entry.focus()
type_entry.bind("<Key-space>", accept_after_space)

start = Button(text="Start", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[4])
start.grid(column=0, row=2)

window.mainloop()
