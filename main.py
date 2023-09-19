import tkinter
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk, ImageOps
from faker import Faker
import math

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

COUNT = 0

timer_r = None

test_in_progress = True

words_writt_prop = 0

# ---------------------------- ACCEPT AFTER SPACE ------------------------------- #
def accept_after_space(event):
    global COUNT
    global test_in_progress
    global words_writt_prop
    if COUNT != 50:
        if COUNT != 0:
            typed_word = type_entry.get()[1:]
        else:
            typed_word = type_entry.get()
        type_entry.delete(0, tkinter.END)

        if typed_word == RANDOM_WORDS[COUNT]:
            exec(f'text_generated_label_{COUNT + 1}.configure(style="Font_2.TLabel")')
            words_writt_prop += 1
        else:
            exec(f'text_generated_label_{COUNT + 1}.configure(style="Font_1.TLabel")')

        if COUNT == 0:
            counting(0)

        if COUNT == 49:
            test_in_progress = False

        COUNT += 1

# ---------------------------- COUNTING MECHANISM ------------------------------- #
def counting(count_time):
    count_min = math.floor(count_time / 60)
    count_sec = count_time % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count_min < 10:
        count_min = f'0{count_min}'
    timer_label.config(text=f'{count_min}:{count_sec}')
    if count_time >= 0 and test_in_progress:
        global timer_r
        timer_r = window.after(1000, counting, count_time + 1)
    if not test_in_progress:
        wpm = words_writt_prop / count_time * 60
        result_label.config(text=f"Congratulations!\nYour WPM is: {int(wpm)}")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Typing Speed Test")
window.config(padx=100, pady=50, bg=COLOUR_PALETTE[0])

#Środkowanie zawartości
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

title = Label(text="Typing Speed Test", font=(FONT_NAME, 35), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[2])
title.grid(column=0, row=0, columnspan=5)

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
    picture.grid(column=0, row=1, columnspan=5, pady=25)

timer_label = Label(text="Type the first word", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[4])
timer_label.grid(column=0, row=2, columnspan=5)

text_label = Label(text="Words to type:", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[4])
text_label.grid(column=0, row=3, pady=25, columnspan=5)

# text_generated_label_1 = ttk.Label(text=RANDOM_WORDS[:5], font=(FONT_NAME, 12))
# style = ttk.Style()
# style.configure("Green.TLabel", foreground=COLOUR_PALETTE[2], background=COLOUR_PALETTE[0])
# text_generated_label_1.grid(column=0, row=4)

style_default = ttk.Style()
style_red = ttk.Style()
style_green = ttk.Style()
style_default.configure("Font_0.TLabel", background=COLOUR_PALETTE[0], foreground=COLOUR_PALETTE[4])
style_red.configure("Font_1.TLabel", background=COLOUR_PALETTE[0], foreground=COLOUR_PALETTE[3])
style_green.configure("Font_2.TLabel", background=COLOUR_PALETTE[0], foreground=COLOUR_PALETTE[2])

nr_of_rows = 10
for j in range(nr_of_rows):
    for i in range(5):
        label_number = i+1 + (j * 5)
        label = f"text_generated_label_{label_number}"
        argument_1 = f"ttk.Label(text=RANDOM_WORDS[{label_number - 1}:{label_number}], font=(FONT_NAME, 12))"
        argument_2 = f".grid(column={i}, row={j + 4})"
        argument_3 = f'.configure(style="Font_0.TLabel")'
        exec(f"{label} = {argument_1}")
        exec(f"{label}{argument_2}")
        exec(f'{label}{argument_3}')



type_label = Label(text="Type here:", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[4])
type_label.grid(column=0, row=14, pady=25, columnspan=5)

result_label = Label(text="", font=(FONT_NAME, 20), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[4])
result_label.grid(column=0, row=16, pady=25, columnspan=5)

type_entry = Entry(width=40, bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[2], justify="center")
type_entry.grid(column=0, row=15, columnspan=5)
type_entry.focus()
type_entry.bind("<Key-space>", accept_after_space)



# start = Button(text="Start", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[4])
# start.grid(column=0, row=2, columnspan=5)

window.mainloop()
