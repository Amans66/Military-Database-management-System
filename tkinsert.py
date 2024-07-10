from tkinter import *
import mysql.connector as mc


class MyWindow:
    def __init__(self, win):
        self.lb = Label(win, text="INSERT", font="STENCIL 20", bg="gold", fg="black")
        self.lb.place(x=205, y=0)
        self.lbl1 = Label(win, text='Service No', font="STENCIL ", relief=RIDGE)
        self.lbl2 = Label(win, text='Name', font="STENCIL ", relief=RIDGE)
        self.lbl3 = Label(win, text='Serving in', font="STENCIL ", relief=RIDGE)
        self.lbl4 = Label(win, text='Rank', font="STENCIL ", relief=RIDGE)
        self.lbl5 = Label(win, text='Trade', font="STENCIL ", relief=RIDGE)
        self.lbl6 = Label(win, text='Unit', font="STENCIL", relief=RIDGE)
        self.lbl7 = Label(win, text=' Massage---> ', relief=RIDGE, font="STENCIL")
        self.t1 = Entry(bd=4)
        self.t2 = Entry(bd=4)
        self.t3 = Entry(bd=4)
        self.t4 = Entry(bd=4)
        self.t5 = Entry(bd=4)
        self.t6 = Entry(bd=4)
        self.t7 = Entry(bd=4)
        self.btn1 = Button(win, text='Insert', relief=RIDGE, font="STENCIL ", bd=5)
        self.btn2 = Button(win, text='Exit', relief=RIDGE, font="STENCIL", bd=5)
        self.lbl1.place(x=100, y=45)
        self.t1.place(x=250, y=45)
        self.lbl2.place(x=100, y=75)
        self.t2.place(x=250, y=75)
        self.lbl3.place(x=100, y=105)
        self.t3.place(x=250, y=107)
        self.lbl4.place(x=100, y=135)
        self.t4.place(x=250, y=135)
        self.lbl5.place(x=100, y=165)
        self.t5.place(x=250, y=165)
        self.lbl6.place(x=100, y=195)
        self.t6.place(x=250, y=195)
        self.b1 = Button(win, text='Insert', font="STENCIL ", bg='green3', fg='white', bd=5, relief=RIDGE,
                         command=self.insert)
        self.b2 = Button(win, text='Exit', bg='red', fg='white', relief=RIDGE, font="STENCIL ", bd=5)
        self.b2.bind('<Button-1>', quit)
        self.b1.place(x=100, y=240)
        self.b2.place(x=200, y=240)
        self.lbl7.place(x=100, y=300)
        self.t7.place(x=250, y=303, width=150)

    def insert(self):
        self.t7.delete(0, 'end')
        e = int(self.t1.get())
        n = self.t2.get()
        mycon = mc.connect(host='localhost', user='root', passwd='1234', database='military', charset='utf8')
        if mycon.is_connected():
            print("connection established sucessfully")
        mycur = mycon.cursor()
        sin = self.t3.get()
        p = self.t4.get()
        t = self.t5.get()
        u = self.t6.get()
        query = f"insert into m_employee values('{e}','{n}','{sin}','{p}','{t}','{u}')"
        mycur.execute(query)
        mycon.commit()
        result = "data inserted sucessfully"
        self.t7.insert(END, str(result))


window = Tk()
mywin = MyWindow(window)
window.title('Insert M_employee')
window.geometry("500x450+10+10")
window.configure(bg="orange")
window.mainloop()
