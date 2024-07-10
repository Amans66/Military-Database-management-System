from tkinter import *
from tkinter import Tk
import display
import tkupdate


root: Tk = Tk()

Frame1 = Frame(root)
Frame1.place(relx=0.20, rely=0.00, relheight=0.20, relwidth=0.60)
Frame1.configure(relief=RIDGE)
Frame1.configure(borderwidth="11")
Frame1.configure(relief=RIDGE)
Frame1.configure(background="#ffffff")
Frame1.configure(highlightbackground="#ffffff")
Frame1.configure(highlightcolor="gold")
Frame1.configure(width=1200)
Frame1.configure(bg="black")
root.geometry("500x480")
root.title(" Military Window ")
root.configure(bg="gold")

Label(root, text="Military DB ", font="STENCIL 30", bg="black", fg="white").place(x=125, y=15)
# Button
Button(root, text=" 1: Display Data ", font="STENCIL 18 bold", bg="black", fg="white",borderwidth="7", command=display.call).place(x=120, y=120)
Button(root, text=" 2: Update Data  ", font="STENCIL 18 bold", bg="black", fg="white",borderwidth="7", command=tkupdate.call).place(x=120,y=170)
Button(root, text=" 3: Search Data  ", font="STENCIL 18 bold", bg="black", fg="white",borderwidth="7").place(x=120,y=220)
Button(root, text=" 4: Delete Data   ", font="STENCIL 18 bold", bg="black", fg="white",borderwidth="7").place(x=120,y=270)
Button(root, text=" 5: Insert Data   ", font="STENCIL 18 bold", bg="black", fg="white",borderwidth="7").place(x=120,y=320)
Button(root, text=" Exit", font="impack 15 bold", bg="Red", fg="white",borderwidth="10", command=root.destroy).place(x=120, y=420)
mainloop()
