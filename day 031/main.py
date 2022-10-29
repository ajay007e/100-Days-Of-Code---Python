from textwrap import fill
import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
WORD = None
TIMER = None

try:
    data = pd.read_csv("day 031/data/word_to_learn.csv")
except:
    pd.read_csv("day 031/data/french_words.csv").to_csv("day 031/data/word_to_learn.csv")
    data = pd.read_csv("day 031/data/word_to_learn.csv")


dic = {}
for (index,row) in data.iterrows():
    dic[index] = [row.English,row.French]

def get_word():
    global TIMER
    TIMER = window.after(3000,switch_card)
    while True:
        try:
            word = dic[random.randint(0,len(dic))]
            break
        except:
            pass
    return word

def cross_btn_click():
    global WORD,TIMER
    if TIMER != None:
        window.after_cancel(TIMER)
    switch_card()
    

def tick_btn_click():
    global WORD,TIMER

    if TIMER != None:
        window.after_cancel(TIMER)
        word = WORD
        # print(data)
        pos = 0
        for (index,row) in data.iterrows():
            if row.English == word[0] and row.French == word[1]:
                pos=index
                break
        # print(pos)
        del dic[pos]
        data.drop(pos,axis=0,inplace=True)
        data.to_csv("day 031/data/word_to_learn.csv",index=False)
        

    WORD = get_word()
    canvas.itemconfig(lang_text,text=WORD[1],fill="black")
    canvas.itemconfig(title_text,text="French",fill="black")
    canvas.itemconfig(canvas_img,image=front_img)

def switch_card():
    global WORD,TIMER
    TIMER= None
    canvas.itemconfig(canvas_img,image=back_img)
    canvas.itemconfig(title_text,text="Engilsh",fill="white")
    canvas.itemconfig(lang_text,text=WORD[0],fill="white")





# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_img = tkinter.PhotoImage(file="day 031/images/card_front.png")
back_img = tkinter.PhotoImage(file="day 031/images/card_back.png")

canvas_img = canvas.create_image(400,263,image=front_img)
canvas.grid(column=0,row=0,columnspan=2)

WORD = get_word()

title_text = canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))
lang_text = canvas.create_text(400,263,text=WORD[1],font=("Arial",60,"bold"))

wrong_img = tkinter.PhotoImage(file="day 031/images/wrong.png")
right_img = tkinter.PhotoImage(file="day 031/images/right.png")


wrong_btn = tkinter.Button(image=wrong_img,highlightthickness=0,command=cross_btn_click)
wrong_btn.grid(column=0,row=1)

right_btn = tkinter.Button(image=right_img,highlightthickness=0,command=tick_btn_click)
right_btn.grid(column=1,row=1)


window.mainloop()