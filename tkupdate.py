from tkinter import *
from tkinter import Tk

import update1
import update2
import update3
def call():
    root: Tk = Tk()

    Frame1 = Frame(root)
    Frame1.place(relx=0.30, rely=0.00, relheight=0.15, relwidth=0.40)
    Frame1.configure(relief=RIDGE)
    Frame1.configure(borderwidth="12")
    Frame1.configure(relief=RIDGE)
    Frame1.configure(background="#ffffff")
    Frame1.configure(highlightbackground="#ffffff")
    Frame1.configure(highlightcolor="gold")
    Frame1.configure(width=995)
    Frame1.configure(bg="black")
    root.geometry("500x480")
    root.title(" Update Window ")
    root.configure(bg="gold")

    Label(root, text="UPDATE", font="STENCIL 25", bg="black", fg="white").place(x=185, y=15)
    # Button
    Button(root, text=" 1: Military Employee", font="impack 18 bold", bg="black", fg="white", command=update1.call).place(
        x=120, y=160)
    Button(root, text=" 2: Military Info", font="impack 18 bold", bg="black", fg="white", command=update2.call).place(x=120,
                                                                                                                      y=250)
    Button(root, text=" 3: Military WTS", font="impack 18 bold", bg="black", fg="white", command=update3.call).place(x=120,
                                                                                                                     y=340)
    Button(root, text=" Exit", font="impack 15 bold", bg="Red", fg="white", command=root.destroy).place(x=120, y=420)
    mainloop()
