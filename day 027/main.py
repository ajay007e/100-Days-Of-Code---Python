import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(500,300)
new_label = tkinter.Label(text="New label",font=('Arial',15,'bold'))
new_label.pack(expand=True)



window.mainloop()