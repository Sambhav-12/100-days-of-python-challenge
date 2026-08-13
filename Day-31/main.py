from tkinter import *
from turtle import heading
from numpy import flip
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv("DAY-31/data/To_Learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("DAY-31/data/french_wrods.csv")
    to_learn = original_data.to_dict(orient="records")
else: 
    to_learn = data.to_dict(orient="records")

new_word = {}

def next_word():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(to_learn)
    canvas.itemconfig(heading_text, text="French", fill="black")
    canvas.itemconfig(word, text=new_word['French'], fill="black")
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_bg, image=card_back)
    canvas.itemconfig(heading_text, text="English", fill="white")
    canvas.itemconfig(word, text=new_word["English"], fill="white")

def is_konwn():
    to_learn.remove(new_word)
    data = pd.DataFrame(to_learn)
    data.to_csv("DAY-31/data/To_Learn.csv", index=False)
    next_word()

window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
# Images
card_front = PhotoImage(file="DAY-31/images/card_front.png")
card_back = PhotoImage(file="DAY-31/images/card_back.png")
right_btn_img = PhotoImage(file="DAY-31/images/right.png")
wrong_btn_img = PhotoImage(file="DAY-31/images/wrong.png")

card_bg = canvas.create_image(400, 263, image=card_front)

canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

heading_text = canvas.create_text(400, 150, text="" , font=("Ariel", 40 , "italic"))
word = canvas.create_text(400, 263, text="" , font=("Ariel", 60 , "bold"))

right_btn = Button(image=right_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=next_word)
right_btn.grid(column=1, row=1)

wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command=is_konwn)
wrong_btn.grid(column=0, row=1)






window.mainloop()


