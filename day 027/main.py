import tkinter

def converter():
    value = float(miles_entry.get())
    value *=1.609
    result.config(text=f"{value}")

window = tkinter.Tk()
window.title("Miles to Km Converter")
window.config(padx=20,pady=20)
# window.minsize(500,300)

miles_entry = tkinter.Entry(width=8)
miles_entry.grid(column=0,row=0)

is_eq = tkinter.Label(text="Is",font=('Arial',15,'normal'),)
is_eq.grid(column=2,row=0)

km = tkinter.Label(text="Kms",font=('Arial',15,'normal'))
km.grid(column=4,row=0)

miles = tkinter.Label(text="Miles",font=('Arial',15,'normal'))
miles.grid(column=1,row=0)

result = tkinter.Label(text="0",font=('Arial',15,'bold'))
result.grid(column=3,row=0)

submit = tkinter.Button(text="Calculate",command=converter)
submit.grid(column=1,row=1,columnspan=3)



window.mainloop()