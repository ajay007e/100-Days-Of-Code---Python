import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("day 031/data/french_words.csv")
dic = {}
for (index,row) in data.iterrows():
    dic[index] = [row.English,row.French]

def get_word():
    return dic[random.randint(0,len(dic))]

def cross_btn_click():
    word = get_word()
    canvas.itemconfig(lang_text,text=word[1])

def tick_btn_click():
    word = get_word()
    canvas.itemconfig(lang_text,text=word[1])

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_img = tkinter.PhotoImage(file="day 031/images/card_front.png")
back_img = tkinter.PhotoImage(file="day 031/images/card_back.png")

canvas.create_image(400,263,image=front_img)
canvas.grid(column=0,row=0,columnspan=2)

word = get_word()

title_text = canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))
lang_text = canvas.create_text(400,263,text=word[1],font=("Arial",60,"bold"))

wrong_img = tkinter.PhotoImage(file="day 031/images/wrong.png")
right_img = tkinter.PhotoImage(file="day 031/images/right.png")


wrong_btn = tkinter.Button(image=wrong_img,highlightthickness=0,command=cross_btn_click)
wrong_btn.grid(column=0,row=1)

right_btn = tkinter.Button(image=right_img,highlightthickness=0,command=tick_btn_click)
right_btn.grid(column=1,row=1)


window.mainloop()