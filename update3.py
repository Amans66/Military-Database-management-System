from tkinter import *
import mysql.connector as mc
def call():
    class MyWindow:
        def __init__(self, win):
            self.lb=Label(win,text="UPDATE",font="STENCIL 18",relief=RIDGE,bg="gold",fg="black",bd=4)
            self.lb.place(x =0, y = 0)
            self.lbl1=Label(win, text='Service No :-',relief=RIDGE,font="arial ")
            self.lbl2=Label(win, text='Choice no :-',relief=RIDGE,font="arial ")
            self.lbl3=Label(win, text=' Massage---> ',relief=RIDGE,font="arial ")
            self.lbl4=Label(win, text='Enter Detail :-',relief=RIDGE,font="arial ")
            a="1:Weaponary & Transpotation System name :- "
            b="2:Weaponary & Transpotation System ID :-"
            c="3:Date & Time OUT"
            d="4:Date & Time IN"
            e="5:REASON"
            g="6:BASE LOCATION"
            f="=======CHOICES========"
            self.lb=Label(win,text =f,font='bold')
            self.lb.place(x = 100, y = 110)
            self.lb=Label(win,text =a,font='bold')
            self.lb.place(x = 100, y = 135)
            self.lb=Label(win,text =b,font='bold')
            self.lb.place(x = 100, y = 159)
            self.lb= Label(win,text =c,font='bold')
            self.lb.place(x = 100, y = 180)
            self.lb=Label(win,text =d,font='bold')
            self.lb.place(x = 100, y = 200)
            self.lb=Label(win,text =e,font='bold')
            self.lb.place(x = 100, y = 220)
            self.lb=Label(win,text =g,font='bold')
            self.lb.place(x = 100, y = 240)
            
            self.t1=Entry(bd=4)
            self.t2=Entry(bd=4)
            self.t3=Entry(bd=4)
            self.t4=Entry(bd=4)
            self.btn1 = Button(win, text='Update',font=" STENCIL ",bd=5)
            self.btn2=Button(win, text='Exit',font=" STENCIL ",bd=5)
            self.lbl1.place(x=100, y=30)
            self.t1.place(x=200, y=30)
            self.lbl4.place(x=100, y=70)
            self.t4.place(x=200, y=70)
            self.lbl2.place(x=100, y=50)
            self.t2.place(x=200, y=50)
            self.b1=Button(win, text='Update',font=" STENCIL ",bg ='green3',fg="white",bd=5,command=self.update)
            self.b2=Button(win, text='Exit',bg ='red',font="STENCIL",bd=5,fg="white",command=win.destroy)
            self.b2.bind('<Button-1>')
            self.b1.place(x=100, y=280)
            self.b2.place(x=200, y=280)
            self.lbl3.place(x=100, y=320)
            self.t3.place(x=200, y=320 ,width=150)
        def update(self):
            self.t3.delete(0, 'end')
            sno=int(self.t1.get())
            ch=int(self.t2.get())
            mycon=mc.connect(host='localhost',user='root',passwd='1234',database='military',charset='utf8')
            if mycon.is_connected():
                 print("connection established sucessfully")
            mycur=mycon.cursor()
            if ch==1:
               g=self.t4.get()
               query=f"update M_wts set wts='{g}' where service_no={sno}"
            elif ch==2:
               d=self.t4.get()
               query=f"update M_wts set WTS_ID ='{d}' where service_no={sno}"
            elif ch==3:
               f=self.t4.get()
               query=f"update M_wts set DT_OUT='{f}' where service_no={sno}"
            elif ch==4:
               m=self.t4.get()
               query=f"update M_WTS set DT_IN='{m}' where service_no={sno}"
            elif ch==5:
               p=self.t4.get()
               query=f"update M_WTS set REASON='{p}' where service_no={sno}"
            elif ch==6:
               s=self.t4.get()
               query=f"update M_WTS set BASE_LOCATION='{s}' where service_no={sno}"
            mycur.execute(query)
            mycon.commit()
            result="data updated sucessfully"
            self.t3.insert(END, str(result))

    window=Tk()
    mywin=MyWindow(window)
    window.title('Update M_WPS')
    window.geometry("500x450+10+10")
    window.configure(bg="orange")
    window.mainloop()

