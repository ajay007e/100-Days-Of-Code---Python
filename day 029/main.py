import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

# timer_label = tkinter.Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45,"bold"))
# timer_label.grid(column=1,row=0)

canvas = tkinter.Canvas(width=200,height=200,highlightthickness=0)
lock_img = tkinter.PhotoImage(file="day 029/logo.png")
canvas.create_image(100,112,image=lock_img)
# timer_text = canvas.create_text(100,140,text="00.00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)

# start_btn = tkinter.Button(text="Start",command=start_timer)
# start_btn.grid(column=0,row=2)

# reset_btn = tkinter.Button(text="Reset",command=reset_timer)
# reset_btn.grid(column=3,row=2)

# check_label = tkinter.Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"normal"))
# check_label.grid(column=1,row=3)

window.mainloop()