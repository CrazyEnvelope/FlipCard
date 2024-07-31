from tkinter import *
import pandas
import random

data_dictionary = {}

try:
    data_read = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dictionary = original_data.to_dict(orient="records")
else:
    data_dictionary = data_read.to_dict(orient="records")

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dictionary)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image = card_front)
    flip_timer=window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text ="English", fill="white")
    canvas.itemconfig(card_word, text =current_card["English"], fill="white")
    canvas.itemconfig(card_background, image = card_back)

def is_known():
    data_dictionary.remove(current_card)
    data = pandas.DataFrame(data_dictionary)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


#---------------------------------GUI------------------------------#
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.minsize(width=800, height=526)
window.title("Flashy")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, background=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column = 0, row = 1)

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, background=BACKGROUND_COLOR, command=is_known)
correct_button.grid(column = 1, row = 1)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800,height=528, background=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400,264,image = card_front)
card_title = canvas.create_text(400,150,text="", font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="", font=("Arial",60,"bold"))
canvas.grid(column = 0 ,row = 0, columnspan=2, sticky = "ew")

next_card()


window.mainloop()

