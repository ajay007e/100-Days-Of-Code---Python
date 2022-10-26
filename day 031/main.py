import tkinter
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_img = tkinter.PhotoImage(file="day 031/images/card_front.png")
back_img = tkinter.PhotoImage(file="day 031/images/card_back.png")

canvas.create_image(400,263,image=front_img)
canvas.grid(column=0,row=0,columnspan=2)



french_text = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
english_text = canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"))

wrong_img = tkinter.PhotoImage(file="day 031/images/wrong.png")
right_img = tkinter.PhotoImage(file="day 031/images/right.png")


wrong_btn = tkinter.Button(image=wrong_img,highlightthickness=0)
wrong_btn.grid(column=0,row=1)

right_btn = tkinter.Button(image=right_img,highlightthickness=0)
right_btn.grid(column=1,row=1)



window.mainloop()