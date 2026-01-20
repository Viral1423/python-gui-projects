from tkinter import *
import time
win=Tk()
win.title("Clock")
win.columnconfigure(0,weight=1)

def clock():
    cur_time=time.strftime("%H:%M:%S %p %a %d-%m-%Y")
    display.delete(0,END)
    display.insert(0,cur_time)
    display.after(1000,clock)

frame=Frame(win)
frame.grid(row=0,column=0,padx=10,pady=10)
label=Label(frame,text="Clock",font=("Times",20))
label.grid(row=0,column=0)
display=Entry(frame,font=("Times",16),width=25,bd=5)
display.grid(row=1,column=0,padx=10,pady=10)
clock()
win.mainloop()
