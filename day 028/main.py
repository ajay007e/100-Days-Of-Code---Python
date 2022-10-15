import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✓"
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global REPS
    REPS = 0 
    if TIMER is not None:
        window.after_cancel(TIMER)
    canvas.itemconfig(timer_text,text="00:00")
    check_label.config(text="")
    timer_label.config(text="Timer",fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    reset_timer()
    global REPS
    REPS +=1
    if REPS % 2 == 1 :
        count_down(60*WORK_MIN)
        timer_label.config(text="Work",fg=GREEN)
    else:
        if REPS % 8 == 0:
            count_down(60*LONG_BREAK_MIN)  
            timer_label.config(text="Break",fg=RED)
        else:
            count_down(60*SHORT_BREAK_MIN)  
            timer_label.config(text="Break",fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    canvas.itemconfig(timer_text,text=f"{count//60}:{str(count%60).zfill(2)}")
    if count > 0 :
        global TIMER
        TIMER = window.after(1000,count_down,count-1)
    else:
        start_timer()
        global REPS,TICK
        ticks = REPS//2 * TICK
        check_label.config(text=ticks)



# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timer_label = tkinter.Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45,"bold"))
timer_label.grid(column=1,row=0)

canvas = tkinter.Canvas(width=206,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="day 028/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,140,text="00.00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)

start_btn = tkinter.Button(text="Start",command=start_timer)
start_btn.grid(column=0,row=2)

reset_btn = tkinter.Button(text="Reset",command=reset_timer)
reset_btn.grid(column=3,row=2)

check_label = tkinter.Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"normal"))
check_label.grid(column=1,row=3)

window.mainloop()