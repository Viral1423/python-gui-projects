from tkinter import *
import random
win=Tk()
win.title("Rocks Paper and Scissors")
choices = ["Rock", "Paper", "Scissors"]
uschoice=Label(win,text="Your Choice:",fg="blue",font=("Times",20))
uschoice.grid(row=0,column=0,padx=10,pady=10)
c1=IntVar()
btn1=Radiobutton(win,text="Rock",variable=c1,value=1,font=("Times",14))
btn1.grid(row=1,column=0)
btn2=Radiobutton(win,text="Paper",variable=c1,value=2,font=("Times",14))
btn2.grid(row=2,column=0)
btn3=Radiobutton(win,text="Scissors",variable=c1,value=3,font=("Times",14))
btn3.grid(row=3,column=0)
def play():
    compchoice=random.choice(choices)
    if uschoice==compchoice:
        label.configure(text="It's a Tie!")
    elif (c1.get()==1 and compchoice=="Scissors") or (c1.get()==2 and compchoice=="Rock") or (c1.get()==3 and compchoice=="Paper"):
        label.configure(text="You Win!")
    else:
        label.configure(text="Computer Wins!")
btns=Button(win,text="Play",command=play,font=("Times",14))
btns.grid(row=4,column=0,padx=10,pady=10)
label=Label(win,text="",fg="blue",font=("Times",20))
label.grid(row=0,column=1,padx=10,pady=10)
win.mainloop()
