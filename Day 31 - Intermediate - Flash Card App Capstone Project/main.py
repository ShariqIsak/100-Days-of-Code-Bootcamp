from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("data/Words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    data = pandas.read_csv("data/Words_to_learn.csv")
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="Black")
    canvas.itemconfig(card_word, text=french_word, fill="Black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English",  fill="White")
    canvas.itemconfig(card_word, text=current_card["English"], fill="White")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/Words_to_learn.csv", index=False)


    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="WORD", font=("Arial", 60, "bold"))

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, command=is_known)
right_button.grid(row=1, column=1)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

next_card()
window.mainloop()
