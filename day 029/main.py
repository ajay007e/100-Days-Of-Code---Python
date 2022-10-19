import tkinter
import pyperclip
from tkinter import messagebox
from random import randint,choice,shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def passwordGenerator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8,10))]
    password_list += [choice(symbols) for _ in range(randint(2,4))]
    password_list += [choice(numbers) for _ in range(randint(2,4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0,len(password_entry.get()))
    password_entry.insert(0,password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    web = web_entry.get()
    
    web_entry.delete(0,len(web))
    try:
        with open("day 029/data.json","r") as f:
            data = json.load(f)
            if web in data.keys():
                data = data[web]
                messagebox.showinfo(title="Info",message=f"username:{data['username']}\npassword:{data['password']}\n")
            else:
                messagebox.showerror(title="Info",message="No Data found")

    except FileNotFoundError:
        messagebox.showerror(title="Info",message="No Data found")

def add():
    web = web_entry.get()
    user = username_entry.get()
    password = password_entry.get()
    dic = {
            web :{
                "username":user,
                "password":password
            }
        }

    if len(web) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showinfo("Opps",message="Please fill data in the required fields")
    else:
        status = messagebox.askokcancel(title=web.title(), message=f"There are the details of you entered :\nEmail:{user}\nPassword:{password}\nIs it okey to continue?")

        if status:
            web_entry.delete(0,len(web))
            password_entry.delete(0,len(password))
            try:
                with open("day 029/data.json","r") as f:
                    data = json.load(f)
                    data.update(dic)
                with open("day 029/data.json","w") as f:
                    json.dump(data,f,indent=4)
            except FileNotFoundError:
                with open("day 029/data.json","w") as f:
                    json.dump(dic,f,indent=4)
                

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

# timer_label = tkinter.Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,45,"bold"))
# timer_label.grid(column=1,row=0)

canvas = tkinter.Canvas(width=200,height=200,highlightthickness=0)
lock_img = tkinter.PhotoImage(file="day 029/logo.png")
canvas.create_image(100,112,image=lock_img)
canvas.grid(column=1,row=0)

web_label = tkinter.Label(text="Website:",pady=5)
web_label.grid(column=0,row=1)

web_entry = tkinter.Entry(width=26)
web_entry.focus()
web_entry.grid(column=1,row=1)

search_btn = tkinter.Button(text="Search",width=14,font=("Ariel",5,"bold"),command=search)
search_btn.grid(column=2,row=1)

username_label = tkinter.Label(text="Email/Username:",pady=5)
username_label.grid(column=0,row=2)

username_entry = tkinter.Entry(width=39)
username_entry.insert(0,"ajay007e")
username_entry.grid(column=1,row=2,columnspan=2)

password_label = tkinter.Label(text="Password:",pady=5)
password_label.grid(column=0,row=3)

password_entry = tkinter.Entry(width=26)
password_entry.grid(column=1,row=3)

generate_password_btn = tkinter.Button(text="Generate Password",font=("Ariel",5,"bold"),command=passwordGenerator)
generate_password_btn.grid(column=2,row=3)

add_btn = tkinter.Button(text="Add",width=36,pady=5,command=add)
add_btn.grid(column=1,row=4,columnspan=2)

window.mainloop()