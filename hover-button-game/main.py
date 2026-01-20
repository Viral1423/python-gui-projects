from tkinter import *
import random 

win = Tk()
win.title("Hover Button Game")
win.geometry("400x400")

label = Label(win, text="Catch the Button!", fg="blue", font=("Times", 20))
label.pack(pady=10)

def change_position(event=None):
    x = random.randint(0, 300)
    y = random.randint(0, 300)
    btn.place(x=x, y=y)

btn = Button(win, text="Catch Me!", bg="yellow", fg="red", font=("Arial", 15))

# Trigger when mouse enters the button
btn.bind("<Enter>", change_position)

btn.place(x=150, y=150)

win.mainloop()
